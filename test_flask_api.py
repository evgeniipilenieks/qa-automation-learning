import requests

BASE_URL = "http://127.0.0.1:5000"

def test_create_and_get_user():
    # 1. Создаём пользователя через API
    payload = {"name": "Анна", "email": "anna@test.com"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == "Анна"
    user_id = data['id']
    
    # 2. Получаем этого пользователя через API
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()['email'] == "anna@test.com"
    
    print(f"Создан и проверен пользователь с ID: {user_id}")