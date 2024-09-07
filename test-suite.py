import pytest
from fastapi.testclient import TestClient
from main import app
from research_tools import ResearchTool
from data_processing import DataProcessor

client = TestClient(app)

@pytest.fixture
def auth_headers():
    response = client.post("/token", data={"username": "demo", "password": "password"})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_login():
    response = client.post("/token", data={"username": "demo", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_protected_route(auth_headers):
    response = client.get("/protected-route", headers=auth_headers)
    assert response.status_code == 200
    assert "Hello, demo" in response.json()["message"]

@pytest.mark.asyncio
async def test_research_tool():
    tool = ResearchTool()
    results = await tool.comprehensive_search("artificial intelligence")
    assert "perplexity" in results
    assert "web_search" in results
    assert "news" in results

@pytest.mark.asyncio
async def test_data_processor():
    processor = DataProcessor()
    test_data = {
        "topic": "Test Topic",
        "findings": ["Finding 1", "Finding 2"],
        "sources": ["Source 1", "Source 2"]
    }
    await processor.process_research_results(test_data)
    search_results = await processor.search_results("Test Topic")
    assert len(search_results) > 0
    assert search_results[0]["topic"] == "Test Topic"

def test_research_endpoint(auth_headers):
    response = client.post("/research", 
                           json={"topic": "climate change", "depth": "medium"},
                           headers=auth_headers)
    assert response.status_code == 200
    assert "findings" in response.json()
    assert "sources" in response.json()

# Add more tests as needed
