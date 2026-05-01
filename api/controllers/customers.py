from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import customers as customers_model

def create(db: Session, customer):


    # Create a new instance of the OrderDetail model with the provided data
    db_customer = customers_model.Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        address=customer.address
    )
    # Add the newly created OrderDetail object to the database session
    db.add(db_customer)
    # Commit the changes to the database
    db.commit()
    # Refresh the OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_customer)
    # Return the newly created OrderDetail object
    return db_customer

def read_all(db: Session):
    return db.query(customers_model.Customer).all()


def read_one(db: Session, item_id):
    return db.query(customers_model.Customer).filter(customers_model.Customer.id == item_id).first()


def update(db: Session, customer_id, customer):
    # Query the database for the specific OrderDetail to update
    db_customer = db.query(customers_model.Customer).filter(customers_model.Customer.id == customer_id)
    # Extract the update data from the provided 'OrderDetail' object
    update_data = customer.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_customer.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated OrderDetail record
    return db_customer.first()



def delete(db: Session, item_id):
    # Query the database for the specific order to delete
    db_customer = db.query(customers_model.Customer).filter(customers_model.Customer.id == item_id)
    # Delete the database record without synchronizing the session
    db_customer.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
