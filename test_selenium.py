import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    """Открываем Chrome перед тестом, закрываем после"""
    d = webdriver.Chrome()
    d.implicitly_wait(5)  # ждём до 5 секунд, если элемент не сразу появляется
    yield d
    d.quit()

def test_python_org_about_link(driver):
    """Находим ссылку 'About' и проверяем её"""
    driver.get("https://www.python.org")
    
    # Находим элемент по частичному тексту ссылки
    about_link = driver.find_element(By.PARTIAL_LINK_TEXT, "About")
    
    # Проверяем: текст ссылки правильный?
    assert about_link.text == "About"
    
    # Проверяем: ссылка ведёт на /about/?
    assert "/about/" in about_link.get_attribute("href")
    
    print(f"Найдена ссылка: {about_link.text} -> {about_link.get_attribute('href')}")

def test_click_about_and_check_title(driver):
    """Кликаем 'About' и проверяем заголовок новой страницы"""
    driver.get("https://www.python.org")
    
    about_link = driver.find_element(By.PARTIAL_LINK_TEXT, "About")
    about_link.click()
    
    # Проверяем: заголовок новой страницы содержит 'About'?
    assert "About" in driver.title, f"Ожидали 'About' в заголовке, а получили: {driver.title}"
    
    print(f"Заголовок после клика: {driver.title}")