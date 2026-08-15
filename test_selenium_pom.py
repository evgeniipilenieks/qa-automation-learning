import pytest
from selenium import webdriver
from pages.python_org_page import PythonOrgPage

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.implicitly_wait(5)
    yield d
    d.quit()

def test_about_page_title(driver):
    page = PythonOrgPage(driver)
    page.open()
    page.click_about()
    assert "About" in page.get_title()