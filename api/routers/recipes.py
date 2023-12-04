from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import recipes as controller
from ..schemas import recipes as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Recipe'],
    prefix="/recipes"
)

# Recipes
@router.post("/recipes/", response_model=schema.Recipe)
def create_recipes(request: schema.RecipeCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/recipes/", response_model=list[schema.Recipe])
def read_all_recipes(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/recipes/{recipe_id}", response_model=schema.Recipe)
def read_one_recipe(item_id: int, db: Session = Depends(get_db)):
    recipe = controller.read_one(db, item_id=item_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.put("/recipes/{recipe_id}", response_model=schema.Recipe, tags=["Recipes"])
def update_recipe(item_id: int, request: schema.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = controller.update(db, request=request, item_id=item_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe_db


@router.delete("/recipes/{recipe_id}", response_model=schema.Recipe, tags=["Recipes"])
def delete_recipe(item_id: int, db: Session = Depends(get_db)):
    recipe = controller.delete(db, item_id=item_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
