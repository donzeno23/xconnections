from pydantic import BaseModel, validator
from models import UserType
from typing import Optional, List

from uuid import uuid4

# class to support creation and update APIs
class CreateAndUpdateUser(BaseModel):
    name: str
    email: str
    password: str | None # blank at signup
    phone: str
    user_type: UserType # vendor or client
    sector: str | None # empty for vendor
    pending: str # Y at signup

    ''' 
    @validator("utypes")
    def user_types_are_valid(cls, utypes):
        user_types = set(item.value for item in UserType)
        if not all(map(lambda x: x in user_types, utypes)):
            raise ValueError("Users must be client or vendor")
        return utypes
    '''


# class to support list and get APIs
class Users(CreateAndUpdateUser):
    user_id: int

    class Config:
        orm_mode = True

class PaginatedUserInfo(BaseModel):
    limit: int
    offset: int
    data: List[Users]