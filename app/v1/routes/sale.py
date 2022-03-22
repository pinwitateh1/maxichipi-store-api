from hashlib import sha256
from typing import List
from fastapi import APIRouter, Response
from app.core.database import conn
from app.core.models.sale import Sale
from app.core.schemas.sale import saleEntity, salesEntity
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

sale = APIRouter(prefix="/sale", tags=['sale'])


@sale.get("/",response_model=List[Sale])
def find_all_sale():
    return salesEntity(conn.maxichipi.sale.find())


@sale.get("/{id}")
def find_sale(id: str):
    return saleEntity(conn.maxichipi.sale.find_one({"_id": ObjectId(id)}))


@sale.post("/")
def create_sale(sale: Sale):
    new_sale = dict(sale)
    id = conn.maxichipi.sale.insert_one(new_sale).inserted_id
    created_sale = conn.maxichipi.sale.find_one({"_id": id})
    return saleEntity(created_sale)


@sale.put("/{id}")
def update_sale(id: str, sale: Sale):
    conn.maxichipi.sale.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(sale)})
    return saleEntity(conn.maxichipi.sale.find_one({"_id": ObjectId(id)}))


@sale.delete("/{id}")
def delete_sale(id: str):
    saleEntity(conn.maxichipi.sale.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
