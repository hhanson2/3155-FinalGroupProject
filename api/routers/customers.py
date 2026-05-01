from fastapi import APIRouter, Depends, FastAPI, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Customers'],
    prefix="/customer"
)


@router.post("/", response_model=schema.Customer)
def create(customer: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, customer=customer)


@router.get("/", response_model=list[schema.Customer])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Customer)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = controller.read_one(db, item_id=item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


@router.put("/{item_id}", response_model=schema.Customer)
def update(customer_id: int, customer: schema.CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, customer=customer, customer_id=customer_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)