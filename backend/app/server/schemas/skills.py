from pydantic import BaseModel
from typing import Optional

from uuid import uuid4

class Skills(BaseModel):
    skill_id: int # auto-generated
    skill: str
