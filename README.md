![Python Tests](https://github.com/evgeniipilenieks/qa-automation-learning/actions/workflows/python-tests.yml/badge.svg)

# QA Automation Learning


# QA Automation Learning

Проект для изучения автоматизации тестирования.  
Стек: Python, pytest, SQL, REST API, Flask, Selenium.

## Технологии

- **Python 3.10+**
- **pytest** — фикстуры, параметризация, assert
- **SQLite + SQL** — JOIN, GROUP BY, LEFT JOIN, агрегатные функции
- **requests** — REST API тесты (GET, POST, JSON)
- **Flask** — собственный тестовый сервер для end-to-end тестирования
- **Selenium WebDriver** — UI-автоматизация браузера
- **Git** — версионирование

## Структура проекта

| Файл | Описание |
|---|---|
| `test_database.py` | Тесты базы данных: SQL + pytest |
| `conftest.py` | Фикстуры pytest (подготовка тестовой БД) |
| `test_api.py` | Тесты публичного REST API (jsonplaceholder) |
| `app.py` | Тестовый Flask-сервер (свой API) |
| `test_flask_api.py` | End-to-end тест: API → База → Проверка |
| `test_selenium.py` | UI-тесты: поиск элементов, клики, проверка заголовков |