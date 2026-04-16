from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order_details as order_details_model

def create(db: Session, order_details):
    # Create a new instance of the OrderDetail model with the provided data
    db_order_details = order_details_model.OrderDetail(
        amount=order_details.amount,
        order_id=order_details.order_id,
        sandwich_id=order_details.sandwich_id
    )
    # Add the newly created OrderDetail object to the database session
    db.add(db_order_details)
    # Commit the changes to the database
    db.commit()
    # Refresh the OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_order_details)
    # Return the newly created OrderDetail object
    return db_order_details


def read_all(db: Session):
    return db.query(order_details_model.OrderDetail).all()


def read_one(db: Session, order_detail_id):
    return db.query(order_details_model.OrderDetail).filter(order_details_model.OrderDetail.id == order_detail_id).first()


def update(db: Session, order_detail_id, order_details):
    # Query the database for the specific OrderDetail to update
    db_order_details = db.query(order_details_model.OrderDetail).filter(order_details_model.OrderDetail.id == order_detail_id)
    # Extract the update data from the provided 'OrderDetail' object
    update_data = order_details.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_order_details.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated OrderDetail record
    return db_order_details.first()


def delete(db: Session, order_detail_id):
    # Query the database for the specific OrderDetail to delete
    db_order_details = db.query(order_details_model.OrderDetail).filter(order_details_model.OrderDetail.id == order_detail_id)
    # Delete the database record without synchronizing the session
    db_order_details.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
