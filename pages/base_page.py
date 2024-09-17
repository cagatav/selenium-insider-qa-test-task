from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
    def wait_for_elements(self, by, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((by, value)))
        return self.driver.find_elements(by, value)
    