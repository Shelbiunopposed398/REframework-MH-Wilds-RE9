import httpx
from typing import List, Dict, Any, Optional
from tavernkeep.config import OLLAMA_BASE_URL

class OllamaService:
    """Service wrapper for interacting with the Ollama LLM REST API."""

    def __init__(self, base_url: str = OLLAMA_BASE_URL):
        self.base_url = base_url.rstrip('/')

    async def check_health(self) -> bool:
        """Check if Ollama server is accessible and responding."""
        try:
            async with httpx.AsyncClient(timeout=3.0) as client:
                response = await client.get(f"{self.base_url}/")
                return response.status_code == 200 or response.text.strip() == "Ollama is running"
        except Exception:
            return False

    async def list_models(self) -> List[Dict[str, Any]]:
        """Fetch list of available local models from Ollama."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                if response.status_code == 200:
                    data = response.json()
                    return data.get("models", [])
                return []
        except Exception as e:
            return []

    async def pull_model(self, model_name: str) -> Dict[str, Any]:
        """Trigger pulling a new model from Ollama library."""
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.base_url}/api/pull",
                    json={"name": model_name, "stream": False}
                )
                if response.status_code == 200:
                    return {"status": "success", "message": f"Model '{model_name}' pulled successfully."}
                return {
                    "status": "error",
                    "message": f"Failed to pull model '{model_name}': HTTP {response.status_code} - {response.text}"
                }
        except Exception as e:
            return {"status": "error", "message": f"Exception while pulling model: {str(e)}"}

    async def delete_model(self, model_name: str) -> Dict[str, Any]:
        """Delete an existing local model from Ollama."""
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.request(
                    "DELETE",
                    f"{self.base_url}/api/delete",
                    json={"name": model_name}
                )
                if response.status_code == 200:
                    return {"status": "success", "message": f"Model '{model_name}' deleted successfully."}
                return {
                    "status": "error",
                    "message": f"Failed to delete model '{model_name}': HTTP {response.status_code}"
                }
        except Exception as e:
            return {"status": "error", "message": f"Exception while deleting model: {str(e)}"}

    async def get_model_info(self, model_name: str) -> Optional[Dict[str, Any]]:
        """Get details and parameters of a specific model."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.post(
                    f"{self.base_url}/api/show",
                    json={"name": model_name}
                )
                if response.status_code == 200:
                    return response.json()
                return None
        except Exception:
            return None
