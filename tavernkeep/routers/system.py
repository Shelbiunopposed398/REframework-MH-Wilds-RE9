import psutil
from fastapi import APIRouter, Depends
from typing import Dict, Any
from tavernkeep.services.ollama_service import OllamaService

router = APIRouter(prefix="/api/system", tags=["System Monitoring"])

def get_ollama_service() -> OllamaService:
    return OllamaService()

@router.get("/health")
async def get_health(service: OllamaService = Depends(get_ollama_service)) -> Dict[str, Any]:
    """Check overall system health and status of connected services."""
    ollama_online = await service.check_health()
    return {
        "status": "healthy",
        "services": {
            "tavernkeep_backend": "online",
            "ollama_llm_engine": "online" if ollama_online else "offline"
        }
    }

@router.get("/stats")
def get_system_stats() -> Dict[str, Any]:
    """Return CPU, RAM, and Disk metrics of the host system."""
    cpu_usage = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "cpu": {
            "usage_percent": cpu_usage,
            "count": psutil.cpu_count(logical=True)
        },
        "memory": {
            "total_bytes": memory.total,
            "available_bytes": memory.available,
            "used_percent": memory.percent
        },
        "disk": {
            "total_bytes": disk.total,
            "free_bytes": disk.free,
            "used_percent": disk.percent
        }
    }
