import sqlite3
import os
import pytest

DB_NAME = 'test_database.db'

@pytest.fixture
def db():
    """Создаёт чистую базу перед каждым тестом"""
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
    
    yield conn
    
    conn.close()
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)