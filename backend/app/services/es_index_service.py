from app.elasticsearch_client import es, INDEX_NAME

def create_index():
    if es.indices.exists(index=INDEX_NAME):
        return

    mapping = {
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "city": {"type": "keyword"},
                "state": {"type": "keyword"},
                "country": {"type": "keyword"},
                "type": {"type": "keyword"},
                "description": {"type": "text"},
                "keywords": {"type": "text"}
            }
        }
    }

    es.indices.create(index=INDEX_NAME, body=mapping)
