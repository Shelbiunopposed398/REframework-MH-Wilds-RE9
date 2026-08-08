import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from tavernkeep.main import app
from tavernkeep.services.ollama_service import OllamaService

client = TestClient(app)

@pytest.mark.asyncio
async def test_list_models_empty():
    with patch.object(OllamaService, "list_models", new_callable=AsyncMock) as mock_list:
        mock_list.return_value = []
        response = client.get("/api/models")
        assert response.status_code == 200
        assert response.json() == []

@pytest.mark.asyncio
async def test_list_models_with_items():
    fake_models = [
        {"name": "llama3:8b", "size": 4700000000, "digest": "sha256:123"},
        {"name": "mistral:7b", "size": 4100000000, "digest": "sha256:456"}
    ]
    with patch.object(OllamaService, "list_models", new_callable=AsyncMock) as mock_list:
        mock_list.return_value = fake_models
        response = client.get("/api/models")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]["name"] == "llama3:8b"

@pytest.mark.asyncio
async def test_pull_model_success():
    with patch.object(OllamaService, "pull_model", new_callable=AsyncMock) as mock_pull:
        mock_pull.return_value = {"status": "success", "message": "Model pulled"}
        response = client.post("/api/models/pull", json={"name": "llama3:8b"})
        assert response.status_code == 200
        assert response.json()["status"] == "success"

@pytest.mark.asyncio
async def test_pull_model_failure():
    with patch.object(OllamaService, "pull_model", new_callable=AsyncMock) as mock_pull:
        mock_pull.return_value = {"status": "error", "message": "Model not found"}
        response = client.post("/api/models/pull", json={"name": "nonexistent:model"})
        assert response.status_code == 400
        assert "Model not found" in response.json()["detail"]

@pytest.mark.asyncio
async def test_delete_model_success():
    with patch.object(OllamaService, "delete_model", new_callable=AsyncMock) as mock_del:
        mock_del.return_value = {"status": "success", "message": "Deleted"}
        response = client.delete("/api/models/llama3:8b")
        assert response.status_code == 200
        assert response.json()["status"] == "success"

@pytest.mark.asyncio
async def test_get_model_info():
    fake_info = {"modelfile": "FROM llama3", "parameters": "stop [INST]"}
    with patch.object(OllamaService, "get_model_info", new_callable=AsyncMock) as mock_info:
        mock_info.return_value = fake_info
        response = client.get("/api/models/llama3:8b/info")
        assert response.status_code == 200
        assert response.json()["modelfile"] == "FROM llama3"
