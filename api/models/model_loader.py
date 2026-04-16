from . import orders, order_details, recipes, sandwiches, resources, menu_items
from . import orders, order_details, recipes, resources, sandwiches
from . import customers, food_categories, ingredients, promotions

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    food_categories.Base.metadata.create_all(engine)
    ingredients.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)

    sandwiches.Base.metadata.create_all(engine)