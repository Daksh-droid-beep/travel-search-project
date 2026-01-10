import json
from app.elasticsearch_client import es, INDEX_NAME
from app.services.es_index_service import create_index

create_index()

with open("cities_ready.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    es.index(
        index=INDEX_NAME,
        document=item
    )

print("✅ Data indexed into Elasticsearch")
