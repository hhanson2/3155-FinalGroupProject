from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menu_items as menu_items_model

def create(db: Session, menu_items):
    # Create a new instance of the OrderDetail model with the provided data
    db_menu_items = menu_items_model.MenuItem(
        name=menu_items.name,
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

def read_all(db: Session):
    return db.query(menu_items_model.MenuItem).all()


def read_one(db: Session, menuItemID):
    return db.query(menu_items_model.MenuItem).filter(menu_items_model.MenuItem.id == menuItemID).first()


def update(db: Session, menuItemID, order):
    # Query the database for the specific order to update
    db_order = db.query(menu_items_model.MenuItem).filter(menu_items_model.MenuItem.id == menuItemID)
    # Extract the update data from the provided 'order' object
    update_data = order.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_order.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order record
    return db_order.first()


def delete(db: Session, menuItemID):
    # Query the database for the specific order to delete
    db_order = db.query(menu_items_model.MenuItem).filter(menu_items_model.MenuItem.id == menuItemID)
    # Delete the database record without synchronizing the session
    db_order.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
