from hashlib import sha256
from typing import List
from fastapi import APIRouter, Response
from app.core.database import conn
from app.core.models.user import User
from app.core.schemas.user import userEntity, usersEntity
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter(prefix="/user", tags=['user'])


@user.get("/",response_model=List[User])
def find_all_user():
    return usersEntity(conn.maxichipi.user.find())


@user.get("/{id}")
def find_user(id: str):
    return userEntity(conn.maxichipi.user.find_one({"_id": ObjectId(id)}))


@user.post("/")
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.hash(new_user["password"])
    id = conn.maxichipi.user.insert_one(new_user).inserted_id
    created_user = conn.maxichipi.user.find_one({"_id": id})
    return userEntity(created_user)


@user.put("/{id}")
def update_user(id: str, user: User):
    conn.maxichipi.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(conn.maxichipi.user.find_one({"_id": ObjectId(id)}))


@user.delete("/{id}")
def delete_user(id: str):
    userEntity(conn.maxichipi.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
