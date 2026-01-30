from pydantic import BaseModel
from typing import Dict, Any

class PerceptionPayload(BaseModel):
    student_id: int
    user_input: str
    signals: Dict[str, Any]
