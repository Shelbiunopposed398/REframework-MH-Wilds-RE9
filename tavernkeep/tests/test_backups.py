import pytest
from fastapi.testclient import TestClient
from pathlib import Path
from tavernkeep.main import app
from tavernkeep.services.backup_service import BackupService
from tavernkeep.routers.backups import get_backup_service

client = TestClient(app)

@pytest.fixture
def temp_backup_env(tmp_path):
    data_dir = tmp_path / "sillytavern"
    data_dir.mkdir()
    
    # Create sample files
    char_file = data_dir / "characters" / "bot.json"
    char_file.parent.mkdir()
    char_file.write_text('{"name": "TestBot", "description": "AI Assistant"}', encoding="utf-8")
    
    backup_dir = tmp_path / "backups"
    backup_dir.mkdir()
    
    service = BackupService(data_dir=data_dir, backup_dir=backup_dir)

    # Override FastAPI dependency
    app.dependency_overrides[get_backup_service] = lambda: service
    yield service, data_dir, backup_dir
    # Cleanup dependency overrides
    app.dependency_overrides.clear()

def test_create_and_list_backup(temp_backup_env):
    service, data_dir, backup_dir = temp_backup_env
    
    # Create backup
    response = client.post("/api/backups", json={"name": "testrun"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    filename = data["filename"]
    
    # List backups
    list_resp = client.get("/api/backups")
    assert list_resp.status_code == 200
    backups = list_resp.json()
    assert len(backups) == 1
    assert backups[0]["filename"] == filename

def test_restore_backup(temp_backup_env):
    service, data_dir, backup_dir = temp_backup_env
    
    # Create a dummy backup
    res = service.create_backup(custom_name="restore_test")
    filename = res["filename"]
    
    # Remove original files
    char_file = data_dir / "characters" / "bot.json"
    if char_file.exists():
        char_file.unlink()
    
    # Restore backup
    restore_resp = client.post(f"/api/backups/{filename}/restore")
    assert restore_resp.status_code == 200, f"Failed: {restore_resp.json()}"
    assert restore_resp.json()["status"] == "success"
    
    # Verify file restored
    assert char_file.exists()
    assert "TestBot" in char_file.read_text(encoding="utf-8")

def test_delete_backup(temp_backup_env):
    service, data_dir, backup_dir = temp_backup_env
    
    res = service.create_backup(custom_name="del_test")
    filename = res["filename"]
    
    del_resp = client.delete(f"/api/backups/{filename}")
    assert del_resp.status_code == 200, f"Failed: {del_resp.json()}"
    assert del_resp.json()["status"] == "success"
    
    list_resp = client.get("/api/backups")
    assert len(list_resp.json()) == 0
