from fastapi import APIRouter, Depends, HTTPException
from fastapi import status, Request
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from server.crud import get_all_users, create_user, get_user_info_by_id, update_user_info, delete_user
from database import get_db
from server.exceptions import UserException
from server.schemas.users import Users, CreateAndUpdateUser, PaginatedUserInfo

import mysql.connector as connector

# Database configuration
db_config = {
  'user': 'daloia',
  'password': 'admin',
  'host': 'localhost',
  'database': 'xconnections',
  'raise_on_warnings': True
}

# Create a connection to the database

cnx = connector.connect(**db_config)
cursor = cnx.cursor()


# from app.api.routes import audit

router = APIRouter()

# router.include_router(audit.router, tags=["audit"], prefix="/audit")

'''
@router.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
'''


@cbv(router)
class UserInfo:
    session: Session = Depends(get_db)

    # API to get the list of users
    @router.get("/users", response_model=PaginatedUserInfo)
    def list_users(self, limit: int = 10, offset: int = 0):

        users_list = get_all_users(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": users_list}

        return response
    
    # API endpoint to add a user to the database
    @router.post("/users") # status_code=status.HTTP_201_CREATED, response_model=CreateAndUpdateUser)
    def add_user(self, user: CreateAndUpdateUser):

        try:
            user = create_user(self.session, user)
            return user
        except UserException as uie:
            # raise HTTPException(**uie.__dict__)
            raise HTTPException(
                status_code= status.HTTP_409_CONFLICT,
                detail='This User is already created!'
      )


# API endpoint to get info of a particular user
@router.get("/users/{user_id}", response_model=Users)
def get_user_info(user_id: int, session: Session = Depends(get_db)):

    try:
        user_info = get_user_info_by_id(session, user_id)
        return user_info
    except UserException as uie:
        raise HTTPException(**uie.__dict__)
    
# API to update an existing user
def update_user(user_id: int, new_info: CreateAndUpdateUser, session: Session = Depends(get_db)):

    try:
        user_info = update_user_info(session, user_id, new_info)
        return user_info
    except UserException as uie:
        raise HTTPException(**uie.__dict__)

# TODO: fix maximum RecursionError
'''
# API to delete a user from the database
@router.delete("/users/{user_id}")
async def delete_user(user_id: int, session: Session = Depends(get_db)):

    try:
        print(f"deleting user: {user_id}")
        # return delete_user(session, user_id)
        await delete_user(session, user_id)
        print(f"user {user_id} was deleted!")
    except UserException as uie:
        raise HTTPException(**uie.__dict__)
'''


# Route to delete an item
# TODO: response mode
# fastapi.exceptions.ResponseValidationError: 5 validation errors:
@router.delete("/users/{user_id}") #, response_model=CreateAndUpdateUser)
def delete_user(user_id: int):
    cursor = cnx.cursor()
    query = "DELETE FROM users WHERE user_id=%s"
    cursor.execute(query, (user_id,))
    cnx.commit()
    cursor.close()
    return {"id": user_id}