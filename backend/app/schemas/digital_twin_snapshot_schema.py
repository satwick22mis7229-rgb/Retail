from pydantic import BaseModel


class DigitalTwinSnapshotCreate(BaseModel):
    store_id: int
    snapshot_payload: dict
    snapshot_version: str = "v1"
    state_hash: str | None = None
    created_by: str = "system"
