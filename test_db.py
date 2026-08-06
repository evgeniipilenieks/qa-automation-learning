import sqlite3
import os
import pytest

DB_NAME = 'my_database.db'

@pytest.fixture
def db():
    """Фикстура: создаёт чистую базу перед тестом и закрывает после"""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, city TEXT)')
    cursor.execute('CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, product TEXT, price INTEGER)')
    
    cursor.execute("INSERT INTO users (name, city) VALUES ('Иван', 'Москва')")
    cursor.execute("INSERT INTO users (name, city) VALUES ('Мария', 'Питер')")
    cursor.execute("INSERT INTO users (name, city) VALUES ('Петр', 'Москва')")
    
    cursor.execute("INSERT INTO orders (user_id, product, price) VALUES (1, 'ноутбук', 50000)")
    cursor.execute("INSERT INTO orders (user_id, product, price) VALUES (1, 'клавиатура', 3000)")
    cursor.execute("INSERT INTO orders (user_id, product, price) VALUES (2, 'мышь', 1500)")
    
    conn.commit()
    
    yield conn  # ← отдаём соединение тесту
    
    conn.close()
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

def test_user_orders_count(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT users.name, orders.product 
        FROM users 
        INNER JOIN orders ON users.id = orders.user_id
    """)
    results = cursor.fetchall()
    assert len(results) == 3

def test_second_order_is_keyboard(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT users.name, orders.product 
        FROM users 
        INNER JOIN orders ON users.id = orders.user_id
        ORDER BY orders.id
    """)
    results = cursor.fetchall()
    assert results[1] == ('Иван', 'клавиатура')

def test_petr_has_no_orders(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT users.name, orders.product 
        FROM users 
        LEFT JOIN orders ON users.id = orders.user_id
        WHERE users.name = 'Петр'
    """)
    result = cursor.fetchone()
    assert result[1] is None
    

@pytest.mark.parametrize("user_name, expected_count", [
    ("Иван", 2),
    ("Мария", 1),
    ("Петр", 0),
])
def test_user_order_count(db, user_name, expected_count):
    cursor = db.cursor()
    cursor.execute("""
        SELECT COUNT(orders.id) 
        FROM users 
        LEFT JOIN orders ON users.id = orders.user_id
        WHERE users.name = ?
    """, (user_name,))
    
    actual_count = cursor.fetchone()[0]
    assert actual_count == expected_count, f"У {user_name} ожидали {expected_count} заказов, а получили {actual_count}"