from sqlalchemy.orm import Session
from sqlalchemy import func, DATETIME
from datetime import date
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as orders_model
from ..models import promotions as promotions_model
import random


def create(db: Session, order):
    promotion_id = None
    if order.promotional_code:
        promotion = db.query(promotions_model.Promotion) \
            .filter(promotions_model.Promotion.code == order.promotional_code) \
            .filter(promotions_model.Promotion.expiration_date >= date.today()) \
            .first()

        if promotion is None:
            raise HTTPException(status_code=400, detail="Invalid or expired promotional code")

        promotion_id = promotion.id  # extract the integer ID
    # Create a new instance of the Order model with the provided data
    db_order = orders_model.Order(
        customer_id=order.customer_id,
        description=order.description,
        order_date=func.now(),
        tracking_number=random.randint(1, 1000),
        promotion_id=promotion_id,
        status="New Order",
        total_price=0.0,
        order_type = order.order_type or "dine-in"
     )
    # Add the newly created Order object to the database session
    db.add(db_order)
    # Commit the changes to the database
    db.commit()
    # Refresh the Order object to ensure it reflects the current state in the database
    db.refresh(db_order)
    # Return the newly created Order object
    return db_order


def read_all(db: Session):
    return db.query(orders_model.Order).all()


def read_one(db: Session, order_id):
    return db.query(orders_model.Order).filter(orders_model.Order.id == order_id).first()


def update(db: Session, order_id, order):
    # Query the database for the specific order to update
    db_order = db.query(orders_model.Order).filter(orders_model.Order.id == order_id)
    # Extract the update data from the provided 'order' object
    update_data = order.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_order.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order record
    return db_order.first()


def delete(db: Session, order_id):
    # Query the database for the specific order to delete
    db_order = db.query(orders_model.Order).filter(orders_model.Order.id == order_id)
    # Delete the database record without synchronizing the session
    db_order.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def read_revenue_of_day(db: Session, aDate: date):
    revenue = db.query(func.sum(orders_model.Order.total_price))\
                .filter(func.date(orders_model.Order.order_date) == aDate)

    if revenue is None:
        raise HTTPException(status_code=404, detail="No revenue found for this date")

    return {"date": date, "total_revenue": revenue}

def read_by_tracking_number(db: Session, tracking_number: int):
    order = db.query(orders_model.Order).filter(orders_model.Order.tracking_number == tracking_number).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order