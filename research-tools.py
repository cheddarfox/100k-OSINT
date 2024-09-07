import httpx
import os
from typing import List, Dict

class ResearchTool:
    def __init__(self):
        self.perplexity_client = httpx.AsyncClient(
            base_url="https://api.perplexity.ai",
            headers={"Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}"}
        )
        self.serper_client = httpx.AsyncClient(
            base_url="https://serpapi.com",
            params={"api_key": os.getenv('SERPER_API_KEY')}
        )
        self.news_client = httpx.AsyncClient(
            base_url="https://newsapi.org/v2",
            params={"apiKey": os.getenv('NEWS_API_KEY')}
        )

    async def perplexity_search(self, query: str) -> Dict:
        response = await self.perplexity_client.post("/query", json={"query": query})
        response.raise_for_status()
        return response.json()

    async def serper_search(self, query: str) -> List[Dict]:
        response = await self.serper_client.get("/search", params={"q": query, "engine": "google"})
        response.raise_for_status()
        return response.json().get("organic", [])

    async def news_search(self, query: str) -> List[Dict]:
        response = await self.news_client.get("/everything", params={"q": query, "sortBy": "relevancy"})
        response.raise_for_status()
        return response.json().get("articles", [])

    async def comprehensive_search(self, query: str) -> Dict:
        perplexity_results = await self.perplexity_search(query)
        serper_results = await self.serper_search(query)
        news_results = await self.news_search(query)

        return {
            "perplexity": perplexity_results,
            "web_search": serper_results[:5],  # Limit to top 5 results
            "news": news_results[:5]  # Limit to top 5 articles
        }

research_tool = ResearchTool()
