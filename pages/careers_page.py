from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
import time

class CareersPage(BasePage):
    def scroll_to_element(self, element):
        """Scroll to the specified element."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def check_find_your_calling(self):
        """Check if the 'Find your calling' title is present and displayed."""
        try:
            find_your_calling_title = self.wait_for_element(By.XPATH, "//h3[contains(text(), 'Find your calling')]")
            assert find_your_calling_title.is_displayed()
            print("The 'Find your calling' title is present and displayed.")
            self.scroll_to_element(find_your_calling_title)
        except NoSuchElementException:
            print("The 'Find your calling' title is not present.")

    def check_our_locations(self):
        """Check if the 'Our Locations' title is present and displayed."""
        try:
            our_locations_title = self.wait_for_element(By.XPATH, "//h3[contains(text(), 'Our Locations')]")
            assert our_locations_title.is_displayed()
            print("The 'Our Locations' title is present and displayed.")
            self.scroll_to_element(our_locations_title)
        except NoSuchElementException:
            print("The 'Our Locations' title is not present.")

    def check_life_at_insider(self):
        """Check if the 'Life at Insider' title is present and displayed."""
        try:
            life_at_insider_title = self.wait_for_element(By.XPATH, "//h2[contains(text(), 'Life at Insider')]")
            assert life_at_insider_title.is_displayed()
            print("The 'Life at Insider' title is present and displayed.")
        except NoSuchElementException:
            print("The 'Life at Insider' title is not present.")