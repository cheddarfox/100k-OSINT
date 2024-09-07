import asyncpg
from elasticsearch import AsyncElasticsearch
import os
from typing import Dict, List

class DataProcessor:
    def __init__(self):
        self.db_url = os.getenv("DATABASE_URL")
        self.es_url = os.getenv("ELASTICSEARCH_URL")
        self.es_client = AsyncElasticsearch(self.es_url)

    async def clean_data(self, data: Dict) -> Dict:
        # Implement data cleaning logic here
        # For example, remove HTML tags, normalize text, etc.
        return data

    async def store_in_postgres(self, data: Dict):
        async with asyncpg.create_pool(self.db_url) as pool:
            async with pool.acquire() as conn:
                await conn.execute("""
                    INSERT INTO research_results (topic, findings, sources)
                    VALUES ($1, $2, $3)
                """, data['topic'], data['findings'], data['sources'])

    async def index_in_elasticsearch(self, data: Dict):
        await self.es_client.index(index="research_results", body=data)

    async def process_research_results(self, results: Dict):
        cleaned_data = await self.clean_data(results)
        await self.store_in_postgres(cleaned_data)
        await self.index_in_elasticsearch(cleaned_data)

    async def search_results(self, query: str) -> List[Dict]:
        response = await self.es_client.search(
            index="research_results",
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["topic", "findings"]
                    }
                }
            }
        )
        return [hit["_source"] for hit in response["hits"]["hits"]]

data_processor = DataProcessor()
