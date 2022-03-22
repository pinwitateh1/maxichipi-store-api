from fastapi import FastAPI
from app.v1.routes.user import user
from app.v1.routes.category import category
from app.v1.routes.product import product
from app.v1.routes.sale import sale

app = FastAPI(
    title="API Maxichipi store"
)

app.include_router(user)
app.include_router(category)
app.include_router(product)
app.include_router(sale)
