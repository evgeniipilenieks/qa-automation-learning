from selenium.webdriver.common.by import By

class PythonOrgPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.python.org"
        self.about_link = (By.PARTIAL_LINK_TEXT, "About")
    
    def open(self):
        self.driver.get(self.url)
    
    def click_about(self):
        self.driver.find_element(*self.about_link).click()
    
    def get_title(self):
        return self.driver.title