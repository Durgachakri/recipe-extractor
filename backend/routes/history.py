from fastapi import APIRouter
from database import SessionLocal
from models import Recipe

router = APIRouter()

@router.get("/recipes")
def get_recipes():
    db = SessionLocal()
    recipes = db.query(Recipe).all()
    db.close()

    return recipes