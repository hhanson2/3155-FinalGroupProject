from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import payment_methods as controller
from ..schemas import payment_methods as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Payment Methods'],
    prefix="/paymenthMethods"
)


@router.post("/", response_model=schema.PaymentMethodBase)
def create(payment_method: schema.PaymentMethodCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, payment_method=payment_method)


@router.get("/", response_model=list[schema.PaymentMethod])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.PaymentMethod)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = controller.read_one(db, item_id=item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


@router.put("/{item_id}", response_model=schema.PaymentMethod)
def update(item_id: int, payment_method: schema.PaymentMethodUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, payment_method=payment_method, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)