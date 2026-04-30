from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menu_items as menu_items_model

def create(db: Session, menu_item):

    ingredientsString = ""
    for ingredient in menu_item.ingredients:
        name = ingredient.name
        amount = ingredient.amount

        stringToAdd = name + ":" + str(amount) + ","

        ingredientsString += stringToAdd

    ingredientsString = ingredientsString[:-1]

    # Create a new instance of the OrderDetail model with the provided data
    db_menu_items = menu_items_model.MenuItem(
        name=menu_item.name,
        description=menu_item.description,
        price=menu_item.price,
        calories=menu_item.calories,
        food_category=menu_item.food_category,
        ingredients= ingredientsString
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


def read_one(db: Session, item_id):
    return db.query(menu_items_model.MenuItem).filter(menu_items_model.MenuItem.id == item_id).first()


def update(db: Session, item_id, menu_item):
    # Query the database for the specific order to update
    db_menu_item = db.query(menu_items_model.MenuItem).filter(menu_items_model.MenuItem.id == item_id)

    ingredientsString = ""
    for ingredient in menu_item.ingredients:
        name = ingredient.name
        amount = ingredient.amount
        stringToAdd = name + ":" + str(amount) + ","
        ingredientsString += stringToAdd
    ingredientsString = ingredientsString[:-1]

    update_data = {
        "name":          menu_item.name,
        "description":   menu_item.description,
        "price":         menu_item.price,
        "calories":      menu_item.calories,
        "food_category": menu_item.food_category,
        "ingredients":   ingredientsString
    }

    db_menu_item.update(update_data, synchronize_session=False)
    db.commit()
    return db_menu_item.first()


def delete(db: Session, item_id):
    # Query the database for the specific order to delete
    db_menu_item = db.query(menu_items_model.MenuItem).filter(menu_items_model.MenuItem.id == item_id)
    # Delete the database record without synchronizing the session
    db_menu_item.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
