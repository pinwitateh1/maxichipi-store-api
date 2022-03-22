from typing import List
from fastapi import APIRouter, Response
from app.core.database import conn
from app.core.models.product import Product
from app.core.schemas.product import productEntity, productsEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

product = APIRouter(prefix="/product", tags=['product'])


@product.get("/",response_model=List[Product])
def find_all_product():
    return productsEntity(conn.maxichipi.product.find())


@product.get("/{id}")
def find_product(id: str):
    return productEntity(conn.maxichipi.product.find_one({"_id": ObjectId(id)}))


@product.post("/")
def create_product(product: Product):
    new_product = dict(product)
    id = conn.maxichipi.product.insert_one(new_product).inserted_id
    created_product = conn.maxichipi.product.find_one({"_id": id})
    return productEntity(created_product)


@product.put("/{id}")
def update_product(id: str, product: Product):
    conn.maxichipi.product.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(product)})
    return productEntity(conn.maxichipi.product.find_one({"_id": ObjectId(id)}))


@product.delete("/{id}")
def delete_product(id: str):
    productEntity(conn.maxichipi.product.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)