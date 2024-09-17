import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../pages')))

from home_page import HomePage
from qa_jobs_page import QAJobsPage  
from careers_page import CareersPage  

def take_screenshot(driver, file_name):
    screenshot_dir = os.path.join(os.path.dirname(__file__), '../screenshots')
    os.makedirs(screenshot_dir, exist_ok=True) 
    file_path = os.path.join(screenshot_dir, file_name)
    driver.save_screenshot(file_path)
    print(f"Screenshot saved: {file_path}")

driver = webdriver.Chrome()

def dismiss_cookie_consent(driver):
    """Close the cookie consent bar."""
    try:
        consent_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
        )
        consent_button.click()
        print("Cookie consent bar closed.")
    except NoSuchElementException:
        print("Cookie consent bar is not visible.")

try:
    driver.get('https://useinsider.com/')

    dismiss_cookie_consent(driver)

    assert "Insider" in driver.title
    print("Home page loaded successfully.")

    home_page = HomePage(driver)

    home_page.navigate_to_careers()
    print("Successfully navigated to the Careers page.")

    assert "Careers" in driver.title
    print("Careers page loaded successfully!")

    careers_page = CareersPage(driver)

    careers_page.check_find_your_calling()

    careers_page.check_our_locations()

    careers_page.check_life_at_insider()

    qa_jobs_page = QAJobsPage(driver)

    qa_jobs_page.navigate_to_qajobs()
    print("Successfully navigated to the QA Jobs page.")

    qa_jobs_page.click_see_all_qa_jobs()
    print("Clicked on the 'See All QA Jobs' button.")

    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(5)

    qa_jobs_page.filter_location(location="Istanbul, Turkey")
    print("Jobs filtered: Location - Istanbul, Turkey.")

    qa_jobs_page.filter_department(department="Quality Assurance")
    print("Jobs filtered: Department - Quality Assurance.")

    qa_jobs_page.check_job_list_presence()

    time.sleep(3)

    qa_jobs_page.check_jobs_details()

    qa_jobs_page.check_and_click_lever_role()

except Exception as e:
    print(f"An error occured.")
    take_screenshot(driver, f"screenshot_{int(time.time())}.png")
finally:
    driver.quit()