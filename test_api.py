import requests

def test_get_user():
    """Получаем пользователя с тестового API"""
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    
    assert response.status_code == 200, f"Ожидали 200, а получили {response.status_code}"
    
    data = response.json()
    assert data["name"] == "Leanne Graham"
    assert "@" in data["email"]
    
    print(f"Пользователь: {data['name']}, email: {data['email']}")

def test_create_post():
    """Создаём пост на тестовом API"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    payload = {
        "title": "Тестовый пост",
        "body": "Это тело поста",
        "userId": 1
    }
    
    response = requests.post(url, json=payload)
    
    assert response.status_code == 201, f"Ожидали 201, а получили {response.status_code}"
    
    data = response.json()
    assert "id" in data
    assert data["title"] == "Тестовый пост"
    
    print(f"Создан пост с ID: {data['id']}")