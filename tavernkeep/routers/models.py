from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from tavernkeep.services.ollama_service import OllamaService

router = APIRouter(prefix="/api/models", tags=["Model Management"])

def get_ollama_service() -> OllamaService:
    return OllamaService()

class PullModelRequest(BaseModel):
    name: str = Field(..., description="Name of the model to pull from Ollama library (e.g. 'llama3:8b')")

class DeleteModelRequest(BaseModel):
    name: str = Field(..., description="Name of the local model to delete")

@router.get("", response_model=List[Dict[str, Any]])
async def list_models(service: OllamaService = Depends(get_ollama_service)):
    """Fetch all locally installed Ollama models."""
    return await service.list_models()

@router.post("/pull")
async def pull_model(
    payload: PullModelRequest,
    service: OllamaService = Depends(get_ollama_service)
):
    """Trigger pulling a model from Ollama."""
    result = await service.pull_model(payload.name)
    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@router.delete("/{model_name}")
async def delete_model(
    model_name: str,
    service: OllamaService = Depends(get_ollama_service)
):
    """Delete a specified local model."""
    result = await service.delete_model(model_name)
    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@router.get("/{model_name}/info")
async def get_model_info(
    model_name: str,
    service: OllamaService = Depends(get_ollama_service)
):
    """Get details for a specific model."""
    info = await service.get_model_info(model_name)
    if not info:
        raise HTTPException(status_code=404, detail=f"Model info for '{model_name}' not found.")
    return info
