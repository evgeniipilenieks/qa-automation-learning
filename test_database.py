import pytest

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
    assert actual_count == expected_count