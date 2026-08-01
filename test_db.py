import sqlite3
import os
DB_NAME = 'my_database.db'

def setup_database():
    """Создаём чистую базу с таблицами и данными"""
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
    conn.close()

def test_user_orders_count():
    """Проверяем: у Ивана 2 заказа в базе"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT users.name, orders.product 
        FROM users 
        INNER JOIN orders ON users.id = orders.user_id
    """)
    results = cursor.fetchall()
    
    assert len(results) == 3, f"Ожидали 3 строки, а получили {len(results)}"
    print("✓ Тест 1 пройден: количество заказов верное")
    
    conn.close()


def test_second_order_is_keyboard():
    """Проверяем: второй заказ — клавиатура Ивана"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT users.name, orders.product 
        FROM users 
        INNER JOIN orders ON users.id = orders.user_id
        ORDER BY orders.id
    """)
    results = cursor.fetchall()
    
    assert results[1] == ('Иван', 'клавиатура')
    print("✓ Тест 2 пройден: второй заказ — клавиатура")
    
    conn.close()

    
def test_petr_has_no_orders():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT users.name, orders.product 
        FROM users 
        LEFT JOIN orders ON users.id = orders.user_id
        WHERE users.name = 'Петр'
    """)
    result = cursor.fetchone()
    
    assert result[1] is None, f"Ожидали None, а получили {result[1]}"
    print("✓ Тест 3 пройден: у Петра нет заказов")
    
    conn.close()

# === ТОЧКА ВХОДА ===
if __name__ == "__main__":
    setup_database()
    test_user_orders_count()
    test_second_order_is_keyboard()
    test_petr_has_no_orders()
    print("\nВсе тесты пройдены!")




