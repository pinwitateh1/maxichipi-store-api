from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    _id: Optional[str]
    name: str
    