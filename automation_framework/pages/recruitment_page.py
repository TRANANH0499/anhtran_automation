from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from base.base_page import BasePage
from time import sleep

class RecruitmentPage(BasePage):
    
    RECRUITMENT = (By.LINK_TEXT, "Recruitment")
    VACANCIES = (By.XPATH, "//a[text()='Vacancies']")
    ADDBUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    VACANCYNAME = (By.XPATH, "//label[text()='Vacancy Name']/../following-sibling::div//input")
    
    # Fixed locators - Tách riêng dropdown và option
    JOB_TITLE_DROPDOWN = (By.XPATH, "//div[@class='oxd-select-wrapper']")   
    AUTOMATION_TESTER_OPTION = (By.XPATH, "//div[@role='listbox']//span[text()='Automation Tester']")
    
    DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Type description here']")
    HIRINGMANAGER = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SAVEBUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
    
    def open_recruitment(self):
        self.click(self.RECRUITMENT)
        self.click(self.VACANCIES)
        self.click(self.ADDBUTTON)
    
    def set_vacancy_name(self, vacancy_name):
        self.get_element(self.VACANCYNAME).send_keys(vacancy_name)
    
    # Method chính để click dropdown và chọn Automation Tester
    def select_automation_tester_job_title(self):
        """
        Click vào dropdown Job Title và chọn option 'Automation Tester'
        """
        try:
            # Step 1: Click để mở dropdown
            dropdown_element = self.wait.until(
                EC.element_to_be_clickable(self.JOB_TITLE_DROPDOWN)
            )
            dropdown_element.click()
            
            # Step 2: Đợi dropdown options xuất hiện và click chọn Automation Tester
            automation_option = self.wait.until(
                EC.element_to_be_clickable(self.AUTOMATION_TESTER_OPTION)
            )
            automation_option.click()
            
            print("Successfully selected 'Automation Tester' from dropdown")
            
        except Exception as e:
            print(f"Error selecting job title: {e}")
            # Fallback: Thử dùng JavaScript click
            self.select_automation_tester_with_js()
    
    # Backup method sử dụng JavaScript
    def select_automation_tester_with_js(self):
        """
        Backup method sử dụng JavaScript để click dropdown và chọn option
        """
        try:
            # Click dropdown bằng JS
            dropdown = self.get_element(self.JOB_TITLE_DROPDOWN)
            self.driver.execute_script("arguments[0].click();", dropdown)
            
            sleep(1)  # Đợi dropdown load
            
            # Click option bằng JS
            option = self.wait.until(
                EC.presence_of_element_located(self.AUTOMATION_TESTER_OPTION)
            )
            self.driver.execute_script("arguments[0].click();", option)
            
            print("Successfully selected using JavaScript fallback")
            
        except Exception as e:
            print(f"JavaScript fallback also failed: {e}")
            raise e
    
    # Generic method cho flexible selection (bonus)
    def select_job_title_by_text(self, job_title_text):
        """
        Generic method để chọn bất kỳ job title nào từ dropdown
        """
        try:
            # Click dropdown
            self.wait.until(EC.element_to_be_clickable(self.JOB_TITLE_DROPDOWN)).click()
            
            # Tạo dynamic locator cho job title cần chọn
            option_locator = (By.XPATH, f"//div[@role='listbox']//span[text()='{job_title_text}']")
            
            # Click option
            self.wait.until(EC.element_to_be_clickable(option_locator)).click()
            
            print(f"Successfully selected '{job_title_text}' from dropdown")
            
        except Exception as e:
            print(f"Error selecting job title '{job_title_text}': {e}")
            raise e
    
    def set_hiring_manager(self, hiring_manager=None):
        """
        Click vào input Hiring Manager, nhập 'test', đợi options xuất hiện và chọn option đầu tiên
        """
        try:
            # Step 1: Click vào input field Hiring Manager
            hiring_manager_input = self.wait.until(
                EC.element_to_be_clickable(self.HIRINGMANAGER)
            )
            hiring_manager_input.click()
            print("Clicked on Hiring Manager input field")
            
            # Step 2: Clear field và nhập "test"
            hiring_manager_input.clear()
            hiring_manager_input.send_keys("test")
            print("Typed 'test' into Hiring Manager field")
            
            # Step 3: Chờ 10 giây để dropdown options xuất hiện
            sleep(10)
            print("Waited 10 seconds for options to appear")
            
            # Step 4: Chọn option đầu tiên
            # Locator cho option đầu tiên trong dropdown suggestions
            first_option_locator = (By.XPATH, "(//div[@role='option'])[1]")
            
            first_option = self.wait.until(
                EC.element_to_be_clickable(first_option_locator)
            )
            first_option.click()
            print("Selected first option from dropdown")
            
        except Exception as e:
            print(f"Error in set_hiring_manager: {e}")
            # Fallback: Thử với JavaScript click
            self.set_hiring_manager_with_js()
    
    def save(self):
        self.get_element(self.SAVEBUTTON).click()
    
    # Main method - Updated để sử dụng method mới
    def add_vacancy(self, vacancy_name):
        try:
            self.open_recruitment()
            self.set_vacancy_name(vacancy_name)
            
            # Sử dụng method mới để select Automation Tester
            self.select_automation_tester_job_title()
            
            self.set_hiring_manager()
            self.save()
            sleep(1000)
            print("Vacancy added successfully!")
            
        except Exception as e:
            print(f"Error adding vacancy: {e}")
            self.driver.save_screenshot("error_vacancy.png")
            raise e