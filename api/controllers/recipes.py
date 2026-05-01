from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import recipes as recipes_model


def create(db: Session, recipe):

    ingredientsString = ""
    for ingredient in recipe.ingredients:
        name = ingredient.name
        amount = ingredient.amount

        stringToAdd = name + ":" + str(amount) + ","

        ingredientsString += stringToAdd

    ingredientsString = ingredientsString[:-1]
    # Create a new instance of the Order model with the provided data
    db_recipe = recipes_model.Recipe(
        menu_item_id= recipe.menu_item_id,
        ingredients= ingredientsString,
        instructions= recipe.instructions
    )
    # Add the newly created Recipe object to the database session
    db.add(db_recipe)
    # Commit the changes to the database
    db.commit()
    # Refresh the Recipe object to ensure it reflects the current state in the database
    db.refresh(db_recipe)
    # Return the newly created Recipe object
    return db_recipe


def read_all(db: Session):
    return db.query(recipes_model.Recipe).all()


def read_one(db: Session, recipe_id):
    return db.query(recipes_model.Recipe).filter(recipes_model.Recipe.id == recipe_id).first()


def update(db: Session, recipe_id, recipe):
    # Query the database for the specific order to update
    db_recipe = db.query(recipes_model.Recipe).filter(recipes_model.Recipe.id == recipe_id)

    ingredientsString = ""
    for ingredient in recipe.ingredients:
        name = ingredient.name
        amount = ingredient.amount
        stringToAdd = name + ":" + str(amount) + ","
        ingredientsString += stringToAdd
    ingredientsString = ingredientsString[:-1]

    update_data = {
        "menu_item_id": recipe.menu_item_id,
        "ingredients": ingredientsString,
        "instructions":   recipe.instructions
    }

    db_recipe.update(update_data, synchronize_session=False)
    db.commit()
    return db_recipe.first()

def delete(db: Session, recipe_id):
    # Query the database for the specific Recipe to delete
    db_recipe = db.query(recipes_model.Recipe).filter(recipes_model.Recipe.id == recipe_id)
    # Delete the database record without synchronizing the session
    db_recipe.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
