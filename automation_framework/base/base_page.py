from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, xpath):
        return self.wait.until(EC.presence_of_element_located(xpath))

    def click(self, xpath):
        self.wait.until(EC.element_to_be_clickable(xpath)).click()

    def set_text(self, xpath, text):
        self.wait.until(EC.presence_of_element_located(xpath)).send_keys(text)
        
    def select_dropdown_by_text(self, xpath, text):
        element = self.wait.until(EC.element_to_be_clickable(xpath)).click()
        select = Select(element)
        select.selct_by_visible_text(text)
    
    def select_by_java_script(self, xpath):
        self.driver.execute_script("arguments[0].click();", xpath)

    