from selenium.webdriver.common.by import By
from base_page import BasePage

class HomePage(BasePage):
    def navigate_to_careers(self):
        company_menu = self.wait_for_element(By.LINK_TEXT, "Company")
        company_menu.click()
        
        careers_link = self.wait_for_element(By.LINK_TEXT, "Careers")
        careers_link.click()