from pydantic import BaseModel
from typing import Optional

from uuid import uuid4

class Vendors(BaseModel):
    vendor_id: int # auto-generated
    user_id: str # foreign-key (Users.user_id)
    address1: str
    address2: str
    city: str
    state: str
    country: str
    zipcode: int
