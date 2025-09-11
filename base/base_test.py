import pytest
from selenium import webdriver
from time import sleep


class BaseTest:
    @pytest.fixture(scope= "class", autouse=True)
    
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")   
        sleep(5)
        request.cls.driver = self.driver
        
        yield
        self.driver.quit()
    # end def