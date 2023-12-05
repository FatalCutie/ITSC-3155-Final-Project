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
@router.post("/", response_model=schema.Recipe)
def create(request: schema.RecipeCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Recipe])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{recipe_id}", response_model=schema.Recipe)
def read_one(item_id: int, db: Session = Depends(get_db)):
    recipe = controller.read_one(db, item_id=item_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.put("/{recipe_id}", response_model=schema.Recipe, tags=["Recipes"])
def update(item_id: int, request: schema.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = controller.update(db, request=request, item_id=item_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe_db


@router.delete("/{recipe_id}", response_model=schema.Recipe, tags=["Recipes"])
def delete(item_id: int, db: Session = Depends(get_db)):
    recipe = controller.delete(db, item_id=item_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
