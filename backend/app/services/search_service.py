from app.database import collection


def search_locations_service(q: str, search_type: str, limit: int, offset: int):

    # Base query: search ONLY in name
    mongo_query = {
        "name": {
            "$regex": q,
            "$options": "i"  # case-insensitive
        }
    }

    # Apply type filter ONLY if not "all"
    if search_type and search_type.lower() != "all":
        mongo_query["type"] = search_type

    # Total matching documents (for pagination)
    total_results = collection.count_documents(mongo_query)

    # Fetch paginated results
    results = list(
        collection.find(mongo_query, {"_id": 0})
        .sort("name", 1)      # 1 = ascending (A → Z)
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
