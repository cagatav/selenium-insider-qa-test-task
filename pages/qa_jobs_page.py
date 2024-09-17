from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import time

class QAJobsPage(BasePage):
    def navigate_to_qajobs(self):
        """Navigate to the QA Jobs page."""
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        time.sleep(2)

    def click_see_all_qa_jobs(self):
        """Click the 'See all QA jobs' button."""
        see_all_jobs_button = self.wait_for_element(By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
        see_all_jobs_button.click()
        time.sleep(2)

    def select_filter_option(self, filter_container_id, option_text):
        """Select the specified filter option."""
        filter_container = self.wait_for_element(By.ID, filter_container_id)
        filter_container.click()

        option_xpath = f"//li[contains(text(), '{option_text}')]"
        option = self.wait_for_element(By.XPATH, option_xpath)
        
        self.driver.execute_script("arguments[0].scrollIntoView();", option)
        option.click()

    def filter_location(self, location):
        """Apply job filters by location."""
        self.select_filter_option("select2-filter-by-location-container", location)
    
    def filter_department(self, department):
        """Apply job filters by department."""
        self.select_filter_option("select2-filter-by-department-container", department) 
        
    def check_job_list_presence(self):
        """Check if the job list is present."""
        try:
            job_list = self.wait_for_element(By.XPATH, "//div[contains(@class, 'position-list-item-wrapper')]")
            assert job_list.is_displayed()
            print("The job list is present and displayed.")
        except NoSuchElementException:
            print("The job list is not present.")
    
    def check_jobs_details(self):
        """Check the details of all jobs."""
        job_items = self.wait_for_elements(By.XPATH, "//div[@id='jobs-list']")

        for job in job_items:
            position = job.find_element(By.XPATH, ".//p[contains(@class, 'position-title font-weight-bold')]").text
            department = job.find_element(By.XPATH, ".//span[contains(@class, 'position-department text-large font-weight-600 text-primary')]").text
            location = job.find_element(By.XPATH, ".//div[contains(@class, 'position-location text-large')]").text
            
            assert "Quality Assurance" in position, f"Error: Position '{position}' does not contain the expected 'Quality Assurance.'"
            assert "Quality Assurance" in department, f"Error: Department '{department}' does not contain the expected 'Quality Assurance.'"
            assert "Istanbul, Turkey" in location, f"Error: Location '{location}' does not contain the expected 'Istanbul, Turkey.'"
        
        print("All jobs meet the filtering criteria.")
    
    def check_and_click_lever_role(self):
        """Check if the 'View Role' button is present on hover and click it."""
        try:
            lever_element = self.wait_for_element(By.XPATH, "//div[contains(@class, 'position-list-item-wrapper bg-light')]")
            
            ActionChains(self.driver).move_to_element(lever_element).perform()
            
            view_role_button = self.wait_for_element(By.XPATH, "//a[contains(@href, 'https://jobs.lever.co/') and contains(text(), 'View Role')]")
            
            if view_role_button.is_displayed():
                view_role_button.click()
                print("Clicked on the 'View Role' button.")
                time.sleep(3)
            else:
                print("The 'View Role' button is not displayed after hover.")
                
        except NoSuchElementException:
            print("The 'Lever' element or 'View Role' button is not present.")
        except Exception as e:
            print(f"An error occurred.")