import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from tavernkeep.main import app
from tavernkeep.services.ollama_service import OllamaService

client = TestClient(app)

@pytest.mark.asyncio
async def test_system_health():
    with patch.object(OllamaService, "check_health", new_callable=AsyncMock) as mock_health:
        mock_health.return_value = True
        response = client.get("/api/system/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["services"]["tavernkeep_backend"] == "online"
        assert data["services"]["ollama_llm_engine"] == "online"

def test_system_stats():
    response = client.get("/api/system/stats")
    assert response.status_code == 200
    data = response.json()
    assert "cpu" in data
    assert "memory" in data
    assert "disk" in data
    assert "usage_percent" in data["cpu"]
    assert "used_percent" in data["memory"]
