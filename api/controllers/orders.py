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
                .filter(func.date(orders_model.Order.order_date) == aDate)\
                .scalar()

    if revenue is None:
        revenue = 0.0

    return {"date": aDate, "total_revenue": float(revenue)}

def read_by_tracking_number(db: Session, tracking_number: int):
    order = db.query(orders_model.Order).filter(orders_model.Order.tracking_number == tracking_number).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def update_total_price(db: Session, order_id: int):
    from ..models import order_details as order_details_model
    from ..models import menu_items as menu_items_model

    order_details = db.query(order_details_model.OrderDetail) \
        .filter(order_details_model.OrderDetail.order_id == order_id).all()

    total = 0.0
    for detail in order_details:
        menu_item = db.query(menu_items_model.MenuItem) \
            .filter(menu_items_model.MenuItem.id == detail.menu_item_id).first()
        if menu_item:
            total += float(menu_item.price) * detail.amount

    db.query(orders_model.Order).filter(orders_model.Order.id == order_id) \
        .update({"total_price": total}, synchronize_session=False)
    db.commit()


def read_by_date_range(db: Session, start_date: date, end_date: date):
    return db.query(orders_model.Order) \
        .filter(func.date(orders_model.Order.order_date) >= start_date) \
        .filter(func.date(orders_model.Order.order_date) <= end_date) \
        .all()