from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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