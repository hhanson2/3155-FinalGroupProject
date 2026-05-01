from . import (orders, order_details, recipes,
               resources, menu_items,
               customers, promotions,
                reviews, payment_methods
               )

from ..dependencies.database import engine
from sqlalchemy import text


def drop_tables():
    with engine.connect() as conn:
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
        conn.execute(text("DROP TABLE IF EXISTS customers"))
        conn.execute(text("DROP TABLE IF EXISTS orders"))
        conn.execute(text("DROP TABLE IF EXISTS promotions"))
        conn.execute(text("DROP TABLE IF EXISTS order_details"))
        conn.execute(text("DROP TABLE IF EXISTS recipes"))
        conn.execute(text("DROP TABLE IF EXISTS resources"))
        conn.execute(text("DROP TABLE IF EXISTS menu_items"))
        conn.execute(text("DROP TABLE IF EXISTS reviews"))
        conn.execute(text("DROP TABLE IF EXISTS sandwiches"))
        conn.execute(text("DROP TABLE IF EXISTS payment_methods"))
        conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))

def index():
    customers.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    payment_methods.Base.metadata.create_all(engine)