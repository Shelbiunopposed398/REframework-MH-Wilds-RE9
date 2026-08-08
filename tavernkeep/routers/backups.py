from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from pathlib import Path
from tavernkeep.services.backup_service import BackupService
from tavernkeep.config import BACKUP_DIR

router = APIRouter(prefix="/api/backups", tags=["Backup & Restore"])

def get_backup_service() -> BackupService:
    return BackupService()

class CreateBackupRequest(BaseModel):
    name: Optional[str] = Field(None, description="Optional custom tag/name for the backup")

@router.get("", response_model=List[Dict[str, Any]])
def list_backups(service: BackupService = Depends(get_backup_service)):
    """List all available backup archives."""
    return service.list_backups()

@router.post("")
def create_backup(
    payload: Optional[CreateBackupRequest] = None,
    service: BackupService = Depends(get_backup_service)
):
    """Create a new zip backup of SillyTavern data."""
    custom_name = payload.name if payload else None
    result = service.create_backup(custom_name=custom_name)
    if result.get("status") == "error":
        raise HTTPException(status_code=500, detail=result.get("message"))
    return result

@router.post("/{filename}/restore")
def restore_backup(
    filename: str,
    service: BackupService = Depends(get_backup_service)
):
    """Restore SillyTavern data from a stored backup zip file."""
    result = service.restore_backup(filename)
    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@router.delete("/{filename}")
def delete_backup(
    filename: str,
    service: BackupService = Depends(get_backup_service)
):
    """Delete a backup archive."""
    result = service.delete_backup(filename)
    if result.get("status") == "error":
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@router.get("/{filename}/download")
def download_backup(filename: str):
    """Download a backup file directly."""
    backup_path = BACKUP_DIR / filename
    if not backup_path.exists() or not backup_path.is_file():
        raise HTTPException(status_code=404, detail="Backup file not found.")
    return FileResponse(
        path=backup_path,
        filename=filename,
        media_type="application/zip"
    )
