from app.elasticsearch_client import es
from app.database import collection

INDEX_NAME = "locations"


def create_index():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(
            index=INDEX_NAME,
            mappings={
                "properties": {
                    "city": {"type": "text"},
                    "state": {"type": "text"},
                    "country": {"type": "text"},
                    "type": {"type": "keyword"},
                    "keywords": {"type": "text"}
                }
            }
        )


def index_data():
    try:
        create_index()
        for doc in collection.find({}, {"_id": 0}):
            es.index(index=INDEX_NAME, document=doc)
        print("✅ Elasticsearch indexing done")
    except Exception as e:
        print("❌ Elasticsearch indexing failed:", e)
