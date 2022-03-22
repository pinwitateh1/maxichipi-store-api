from typing import List
from fastapi import APIRouter, Response
from app.core.database import conn
from app.core.models.category import Category
from app.core.schemas.category import categoryEntity, categoriesEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

category = APIRouter(prefix="/category", tags=['category'])


@category.get("/",response_model=List[Category])
def find_all_category():
    return categoriesEntity(conn.maxichipi.category.find())


@category.get("/{id}")
def find_category(id: str):
    return categoryEntity(conn.maxichipi.category.find_one({"_id": ObjectId(id)}))


@category.post("/")
def create_category(category: Category):
    new_category = dict(category)
    id = conn.maxichipi.category.insert_one(new_category).inserted_id
    created_category = conn.maxichipi.category.find_one({"_id": id})
    return categoryEntity(created_category)


@category.put("/{id}")
def update_category(id: str, category: Category):
    conn.maxichipi.category.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(category)})
    return categoryEntity(conn.maxichipi.category.find_one({"_id": ObjectId(id)}))


@category.delete("/{id}")
def delete_category(id: str):
    categoryEntity(conn.maxichipi.category.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)