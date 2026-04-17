from fastapi import FastAPI
from database import SessionLocal, engine
from models import Base, Recipe
from scraper import extract_recipe
from utils import *
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.post("/extract")
def extract(url: str):
    db = SessionLocal()

    scraped = extract_recipe(url)

    result = {
        "url": url,
        "title": scraped["title"],
        "cuisine": "Unknown",
        "prep_time": "N/A",
        "cook_time": "N/A",
        "total_time": "N/A",
        "servings": 2,
        "difficulty": "easy",
        "ingredients": scraped["ingredients"],
        "instructions": scraped["instructions"],
        "nutrition_estimate": generate_nutrition(),
        "substitutions": generate_substitutions(),
        "shopping_list": generate_shopping_list(scraped["ingredients"]),
        "related_recipes": generate_related()
    }

    db_recipe = Recipe(
        url=url,
        title=result["title"],
        data=json.dumps(result)
    )

    db.add(db_recipe)
    db.commit()
    db.close()

    return result


@app.get("/recipes")
def get_recipes():
    db = SessionLocal()
    recipes = db.query(Recipe).all()
    db.close()

    return [
        {
            "id": r.id,
            "title": r.title,
            "data": json.loads(r.data)
        }
        for r in recipes
    ]