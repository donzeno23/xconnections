from pydantic import BaseModel
from typing import Optional

from uuid import uuid4

class VendorSkills(BaseModel):
    vs_id: int # auto-generated
    vs_vendor_id: int # foreign-key (Vendors.vendor_id)
    vs_skill_id: int # foreign-key (Skills.skill_id)
