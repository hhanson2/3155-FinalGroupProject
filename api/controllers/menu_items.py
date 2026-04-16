from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menu_items as menu_items_model

def create(db: Session, menu_items):
    # Create a new instance of the OrderDetail model with the provided data
    db_menu_items = menu_items_model.MenuItem(
        amount=menu_items.amount,
        order_id=menu_items.order_id,
        sandwich_id=menu_items.sandwich_id
    )
    # Add the newly created OrderDetail object to the database session
    db.add(db_menu_items)
    # Commit the changes to the database
    db.commit()
    # Refresh the OrderDetail object to ensure it reflects the current state in the database
    db.refresh(db_menu_items)
    # Return the newly created OrderDetail object
    return db_menu_items
