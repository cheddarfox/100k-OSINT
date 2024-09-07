from elasticsearch import Elasticsearch
import os

es = Elasticsearch([os.getenv("ELASTICSEARCH_URL")])

index_name = "research_results"
index_mapping = {
    "mappings": {
        "properties": {
            "topic": {"type": "text"},
            "findings": {"type": "text"},
            "sources": {"type": "keyword"},
            "created_at": {"type": "date"},
            "updated_at": {"type": "date"}
        }
    }
}

# Create the index with the mapping
es.indices.create(index=index_name, body=index_mapping, ignore=400)

# Use this in your data_processing.py file when indexing documents
