from typing import List, Optional

from pydantic import BaseModel


class Sale(BaseModel):
    _id: Optional[str]
    total: int
    comment: str
    categories: List
    products: List

    
    