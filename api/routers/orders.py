from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from datetime import date
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, order=request)


@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/track/{tracking_number}", response_model=schema.Order)
def read_by_tracking_number(tracking_number: int, db: Session = Depends(get_db)):
    return controller.read_by_tracking_number(db, tracking_number=tracking_number)

@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id=item_id)


@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, order_id=item_id, order=request)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_id=item_id)

@router.get("/{date}", response_model=schema.Order)
def read_revenue_of_day(aDate: date, db: Session = Depends(get_db)):
    return controller.read_revenue_of_day(db=db, aDate=aDate)