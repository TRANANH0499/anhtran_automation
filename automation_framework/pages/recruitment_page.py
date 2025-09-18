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
    JOBTITLE = (By.XPATH, "//div[@role='listbox']//span[text()='Automation Tester']")
    DROP_DOWN = (By.XPATH, "//div[@class='oxd-select-wrapper']")   
    DROP_DOWN_OPTION = (By.XPATH, "//div[@role='listbox']//span[text()='Automation Tester']")
    DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Type description here']")
    POSITION = (By.XPATH, "//div[@role='option' and normalize-space(text())='{job_title}']")
    HIRINGMANAGER = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SAVEBUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    
    def open_recruitment(self):
        self.click(self.RECRUITMENT)
        self.click(self.VACANCIES)
        self.click(self.ADDBUTTON)

    def set_vacancy_name(self, vacancy_name):
        self.get_element(self.VACANCYNAME).send_keys(vacancy_name)

    def select_job_title(self, span_xpath):
        self.get_element(self.JOBTITLE).click()
        self.driver.execute_script("arguments[0].click();", span_xpath)
        
    def set_hiring_manager(self, hiring_manager):
        self.get_element(self.HIRINGMANAGER).send_keys(hiring_manager)

    def save(self):
        self.get_element(self.SAVEBUTTON).click()
    
    
    def select_text_from_dropdown(self):
        self.get_element(self.DROP_DOWN).click()
        self.select_by_java_script(self.OPTION)
        self.get_element(self.DROP_DOWN_OPTION).click()

    
    def add_vacancy(self, vacancy_name, job_title, hiring_manager):
        """Thực hiện full flow thêm Vacancy"""
        self.open_recruitment()
        self.set_vacancy_name(vacancy_name)
        self.select_job_title(job_title)
        self.set_hiring_manager(hiring_manager)
        self.select_text_from_dropdown()
        self.save()


