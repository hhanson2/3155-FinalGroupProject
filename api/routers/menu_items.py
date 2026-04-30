from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas import menu_items as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menuitems"
)


@router.post("/", response_model=schema.MenuItemsBase)
def create(menu_item: schema.MenuItemsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, menu_item=menu_item)


@router.get("/", response_model=list[schema.MenuItems])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.MenuItems)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = controller.read_one(db, item_id=item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


@router.put("/{item_id}", response_model=schema.MenuItems)
def update(item_id: int, menu_item: schema.MenuItemsUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, menu_item=menu_item, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)