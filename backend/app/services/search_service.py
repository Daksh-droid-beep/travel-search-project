from app.database import collection
from app.elasticsearch_client import es, INDEX_NAME
from elasticsearch import NotFoundError

def search_locations_service(q: str, search_type: str, limit: int, offset: int):

    es_results = []
    total_es_results = 0

    try:
        es_query = {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": q,
                            "fields": ["name^3", "description", "keywords"]
                        }
                    }
                ]
            }
        }

        if search_type != "all":
            es_query["bool"]["filter"] = [
                {"term": {"type": search_type}}
            ]

        es_response = es.search(
            index=INDEX_NAME,
            from_=offset,
            size=limit,
            query=es_query
        )

        total_es_results = es_response["hits"]["total"]["value"]

        es_results = [
            {
                "name": hit["_source"]["name"],
                "city": hit["_source"].get("city", ""),
                "description": hit["_source"].get("description", ""),
                "type": hit["_source"].get("type", ""),
                "score": hit["_score"]
            }
            for hit in es_response["hits"]["hits"]
        ]

    except NotFoundError:
        # Index not found → fallback to Mongo
        pass

    except Exception as e:
        print("Elasticsearch error:", e)
        pass

    # 🔁 FALLBACK (YOUR ORIGINAL LOGIC — UNTOUCHED)
    if not es_results:
        mongo_query = {
            "$or": [
                {"name": {"$regex": q, "$options": "i"}}
            ]
        }

        if search_type != "all":
            mongo_query["type"] = search_type

        total_results = collection.count_documents(mongo_query)

        results = list(
            collection.find(mongo_query, {"_id": 0})
            .sort("name", 1)
            .skip(offset)
            .limit(limit)
        )

        return {
            "query": q,
            "total_results": total_results,
            "limit": limit,
            "offset": offset,
            "results": results
        }

    return {
        "query": q,
        "total_results": total_es_results,
        "limit": limit,
        "offset": offset,
        "results": es_results
    }
