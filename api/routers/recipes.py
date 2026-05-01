from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import recipes as controller
from ..schemas import recipes as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Recipe'],
    prefix="/recipes"
)


@router.post("/", response_model=schema.RecipeCreate)
def create(recipe: schema.RecipeCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, recipe=recipe)


@router.get("/", response_model=list[schema.Recipe])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Recipe)
def read_one(recipe_id: int, db: Session = Depends(get_db)):
    item = controller.read_one(db, recipe_id=recipe_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


@router.put("/{item_id}", response_model=schema.Recipe)
def update(recipe_id: int, recipe: schema.RecipeUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, recipe=recipe, recipe_id=recipe_id)


@router.delete("/{item_id}")
def delete(recipe_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, recipe_id=recipe_id)