from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import payment_methods as payment_methods_model

def create(db: Session, payment_method):
    # Create a new instance of the OrderDetail model with the provided data
    db_payment_methods = payment_methods_model.PaymentMethod(
        customer_id=payment_method.customer_id,
        type=payment_method.type,
        expiry_date=payment_method.expiry_date,
        card_number=payment_method.card_number
    )
    # Add the newly created OrderDetail object to the database session
    db.add(db_payment_methods)
    # Commit the changes to the database
    db.commit()
    # Refresh the OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_payment_methods)
    # Return the newly created OrderDetail object
    return db_payment_methods

def read_all(db: Session):
    return db.query(payment_methods_model.PaymentMethod).all()


def read_one(db: Session, item_id):
    return db.query(payment_methods_model.PaymentMethod).filter(payment_methods_model.PaymentMethod.id == item_id).first()


def update(db: Session, item_id, payment_method):
    # Query the database for the specific OrderDetail to update
    db_payment_methods = db.query(payment_methods_model.PaymentMethod).filter(payment_methods_model.PaymentMethod.id == item_id)
    # Extract the update data from the provided 'OrderDetail' object
    update_data = payment_method.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_payment_methods.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated OrderDetail record
    return db_payment_methods.first()


def delete(db: Session, item_id):
    # Query the database for the specific order to delete
    db_payment_methods = db.query(payment_methods_model.PaymentMethod).filter(payment_methods_model.PaymentMethod.id == item_id)
    # Delete the database record without synchronizing the session
    db_payment_methods.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
