import pytest
from selenium.webdriver.common.by import By
from base.base_test import BaseTest as BaseTest
from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep
class TestLogin(BaseTest):
    
    USERNAME_INPUT = (By.NAME,"username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_INPUT    = (By.XPATH, "//button[@type='submit']")
    
    def test_login(self):
        username = self.driver.find_element(*self.USERNAME_INPUT)
        password = self.driver.find_element(*self.PASSWORD_INPUT)
        username.send_keys('Admin')
        password.send_keys('admin123')        
        btnlogin = self.driver.find_element(*self.LOGIN_INPUT)
            
        btnlogin.click()
        sleep(7)  # import time
        
