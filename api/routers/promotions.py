from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)

@router.post("/", response_model=schema.Promotion)
def create(promotion: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, promotion=promotion)

@router.get("/", response_model=list[schema.Promotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{promotion_id}", response_model=schema.Promotion)
def read_one(promotion_id: int, db: Session = Depends(get_db)):
    item = controller.read_one(db, promotion_id=promotion_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return item

@router.put("/{promotion_id}", response_model=schema.Promotion)
def update(promotion_id: int, promotion: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, promotion=promotion, promotion_id=promotion_id)

@router.delete("/{promotion_id}")
def delete(promotion_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, promotion_id=promotion_id)