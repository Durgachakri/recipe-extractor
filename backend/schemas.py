from pydantic import BaseModel
from typing import Any

class RecipeCreate(BaseModel):
    url: str

class RecipeResponse(BaseModel):
    id: int
    url: str
    title: str
    cuisine: str
    difficulty: str
    data: Any

    class Config:
        orm_mode = True