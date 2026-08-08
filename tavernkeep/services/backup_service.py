import zipfile
import shutil
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from tavernkeep.config import SILLYTAVERN_DATA_DIR, BACKUP_DIR

class BackupService:
    """Service handling backup creation, restoration, listing, and deletion for SillyTavern data."""

    def __init__(self, data_dir: Path = SILLYTAVERN_DATA_DIR, backup_dir: Path = BACKUP_DIR):
        self.data_dir = data_dir
        self.backup_dir = backup_dir

    def create_backup(self, custom_name: Optional[str] = None) -> Dict[str, Any]:
        """Create a zip archive containing all SillyTavern characters, chats, and configurations."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"tavernkeep_backup_{timestamp}.zip"
        if custom_name:
            sanitized = "".join([c for c in custom_name if c.isalnum() or c in ("-", "_")]).strip()
            if sanitized:
                filename = f"tavernkeep_backup_{sanitized}_{timestamp}.zip"

        backup_path = self.backup_dir / filename

        try:
            with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                if self.data_dir.exists():
                    for file_path in self.data_dir.rglob("*"):
                        if file_path.is_file():
                            arcname = file_path.relative_to(self.data_dir)
                            zip_file.write(file_path, arcname)

            file_size = backup_path.stat().st_size if backup_path.exists() else 0
            return {
                "status": "success",
                "filename": filename,
                "path": str(backup_path),
                "size_bytes": file_size,
                "created_at": timestamp
            }
        except Exception as e:
            if backup_path.exists():
                backup_path.unlink()
            return {"status": "error", "message": f"Failed to create backup: {str(e)}"}

    def list_backups(self) -> List[Dict[str, Any]]:
        """List all available backup archives sorted by creation time (newest first)."""
        backups = []
        if not self.backup_dir.exists():
            return backups

        for zip_file in sorted(self.backup_dir.glob("*.zip"), key=lambda f: f.stat().st_mtime, reverse=True):
            stat = zip_file.stat()
            backups.append({
                "filename": zip_file.name,
                "size_bytes": stat.st_size,
                "modified_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime))
            })
        return backups

    def restore_backup(self, filename: str) -> Dict[str, Any]:
        """Restore SillyTavern data directory from a target backup zip file."""
        backup_path = self.backup_dir / filename
        if not backup_path.exists() or not backup_path.is_file():
            return {"status": "error", "message": f"Backup file '{filename}' not found."}

        try:
            # Ensure target data dir exists
            self.data_dir.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(backup_path, 'r') as zip_file:
                zip_file.extractall(self.data_dir)

            return {
                "status": "success",
                "message": f"Successfully restored data from '{filename}'."
            }
        except Exception as e:
            return {"status": "error", "message": f"Failed to restore backup: {str(e)}"}

    def delete_backup(self, filename: str) -> Dict[str, Any]:
        """Delete a specified backup file from storage."""
        backup_path = self.backup_dir / filename
        if not backup_path.exists() or not backup_path.is_file():
            return {"status": "error", "message": f"Backup file '{filename}' not found."}

        try:
            backup_path.unlink()
            return {"status": "success", "message": f"Backup '{filename}' deleted."}
        except Exception as e:
            return {"status": "error", "message": f"Failed to delete backup: {str(e)}"}
