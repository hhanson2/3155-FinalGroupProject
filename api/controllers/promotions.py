from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import promotions as promotions_model


def create(db: Session, promotion):
    # Create a new instance of the Sandwich model with the provided data
    db_promotion = promotions_model.Promotion(
        code=promotion.code,
        discount_percent=promotion.discount_percent,
        expiration_date=promotion.expiration_date,
    )
    # Add the newly created Sandwich object to the database session
    db.add(db_promotion)
    # Commit the changes to the database
    db.commit()
    # Refresh the Sandwich object to ensure it reflects the current state in the database
    db.refresh(db_promotion)
    # Return the newly created Sandwich object
    return db_promotion

def read_all(db: Session):
    return db.query(promotions_model.Promotion).all()

def read_one(db: Session, promotion_id):
    return db.query(promotions_model.Promotion).filter(promotions_model.Promotion.id == promotion_id).first()

def update(db: Session, promotion_id, promotion):
    # Query the database for the specific Sandwich to update
    db_promotion = db.query(promotions_model.Promotion).filter(promotions_model.Promotion.id == promotion_id)
    # Extract the update data from the provided 'Sandwich' object
    update_data = promotion.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_promotion.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated Sandwich record
    return db_promotion.first()


def delete(db: Session, promotion_id):
    # Query the database for the specific Sandwich to delete
    db_promotion = db.query(promotions_model.Promotion).filter(promotions_model.Promotion.id == promotion_id)
    # Delete the database record without synchronizing the session
    db_promotion.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)