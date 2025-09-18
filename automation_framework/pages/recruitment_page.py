from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation_framework.base.base_page import BasePage


class RecruitmentPage(BasePage):
    
    RECRUITMENT = (By.LINK_TEXT, "Recruitment")
    VACANCIES = (By.XPATH, "//a[text()='Vacancies']")
    ADDBUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    VACANCYNAME = (By.XPATH, "//label[text()='Vacancy Name']/following-sibling::div//input")
    JOBTITLE = (By.XPATH, "//i[contains(@class,'oxd-icon bi-caret-down-fill oxd-select-text--arrow')]")
    OPTION = "//div[@role='option' and normalize-space(text())='{job_title}']"
    HIRINGMANAGER = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SAVEBUTTON = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    
    def open_recruitment(self):
        self.wait.until(EC.element_to_be_clickable(self.RECRUITMENT)).click()
        self.wait.until(EC.element_to_be_clickable(self.VACANCIES)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADDBUTTON)).click()

    def set_vacancy_name(self, vacancy_name):
        self.wait.until(EC.visibility_of_element_located(self.VACANCYNAME)).send_keys(vacancy_name)

    def select_job_title(self, job_title):
        self.wait.until(EC.element_to_be_clickable(self.JOBTITLE)).click()
        option_xpath = (By.XPATH, self.OPTION.format(job_title=job_title))
        self.wait.until(EC.visibility_of_element_located(option_xpath)).click()

    def set_hiring_manager(self, hiring_manager):
        self.wait.until(EC.visibility_of_element_located(self.HIRINGMANAGER)).send_keys(hiring_manager)

    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVEBUTTON)).click()

    
    def add_vacancy(self, vacancy_name, job_title, hiring_manager):
        """Thực hiện full flow thêm Vacancy"""
        self.open_recruitment()
        self.set_vacancy_name(vacancy_name)
        self.select_job_title(job_title)
        self.set_hiring_manager(hiring_manager)
        self.save()


