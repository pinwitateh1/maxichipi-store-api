from typing import List, Optional

from pydantic import BaseModel


class Product(BaseModel):
    _id: Optional[str]
    name: str
    categories: List
    