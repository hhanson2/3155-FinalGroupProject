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

def populate():
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO customers (name, email, phone, address) VALUES ('Samuel', 'test@email.com', '123456', '123 Main St')"))
        conn.execute(text("INSERT INTO customers (name, email, phone, address) VALUES ('Marvin', 'test@email.com', '123456', '123 Main St')"))
        conn.execute(text("INSERT INTO customers (name, email, phone, address) VALUES ('Hanson', 'test@email.com', '123456', '123 Main St')"))
        # Resources
        conn.execute(text("INSERT INTO resources (item, amount) VALUES ('potato', 5)"))
        # Menu Items
        conn.execute(text(
            "INSERT INTO menu_items (name, description, price, calories, food_category) VALUES ('fries', 'super yummy', 5, 80, 'regular')"))
        conn.execute(text(
            "INSERT INTO menu_items (name, description, price, calories, food_category) VALUES ('salad', 'healthy', 6, 10, 'vegan')"))
        # Promotion
        conn.execute(
            text("INSERT INTO promotions (code, discount_percent, expiration_date) VALUES ('None', 0, '2999-05-03')"))
        conn.execute(
            text("INSERT INTO promotions (code, discount_percent, expiration_date) VALUES ('deal', 10, '2026-05-03')"))
        # Payment Method
        conn.execute(text(
            "INSERT INTO payment_methods (customer_id, type, expiry_date, card_number) VALUES (1, 'Credit', '07/33', '123456')"))
        #Order
        conn.execute(text(
            "INSERT INTO orders (customer_id, description, promotion_id, tracking_number, status, total_price, order_type, order_date) VALUES (1, 'My first meal', (SELECT id FROM promotions WHERE code = 'deal'), '123', 'New Order', 0.0, 'dine-in', NOW())"))
        #Order details
        conn.execute(text("INSERT INTO order_details (order_id, menu_item_id, amount) VALUES (1, 1, 1)"))
        #reviews
        conn.execute(
            text("INSERT INTO reviews (review_text, score, customer_id, order_id) VALUES ('This was good', 8, 1, 1)"))
        conn.execute(
            text("INSERT INTO reviews (review_text, score, customer_id, order_id) VALUES ('This was bad', 3, 1, 1)"))
        conn.commit()