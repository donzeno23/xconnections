from typing import List
from sqlalchemy.orm import Session

from server.exceptions import UserAlreadyExistError, UserNotFoundError
from models import Users
from server.schemas.users import CreateAndUpdateUser


# Function to get list of users
def get_all_users(session: Session, limit: int, offset: int) -> List[Users]:
    return session.query(Users).offset(offset).limit(limit).all()

# Function to get info of a particular user
def get_user_info_by_id(session: Session, _id: int) -> Users:
    user = session.query(Users).get(_id)

    if user is None:
        raise UserNotFoundError
    
    return user

# Function to add a new user to the database
def create_user(session: Session, users: CreateAndUpdateUser) -> Users:

    user_details = session.query(Users).filter(Users.name == users.name, Users.email == users.email).first()
    if user_details is not None:
        raise UserAlreadyExistError
    
    new_user = Users(**users.dict())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

# Function to update details of the user
def update_user_info(session: Session, _id: int, user_update: CreateAndUpdateUser) -> Users:
    user = get_user_info_by_id(session, _id)

    if user is None:
        raise UserNotFoundError
    
    user.name = user_update.name
    user.email = user_update.email
    user.phone = user_update.phone
    user.sector = user_update.sector
    user.pending = user_update.pending

    session.commit()
    session.refresh(user)

    return user

# Function to delete a user from the db
def delete_user(session: Session, _id: int):
    user = get_user_info_by_id(session, _id)

    if user is None:
        raise UserNotFoundError
    
    session.delete(user)
    session.commit()

    return