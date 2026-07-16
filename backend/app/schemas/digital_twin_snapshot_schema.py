from pydantic import BaseModel


class DigitalTwinSnapshotCreate(BaseModel):
    store_id: int
    snapshot_payload: dict
