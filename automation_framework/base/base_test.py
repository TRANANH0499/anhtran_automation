import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(scope= "class", autouse=True)
    
    def setup(self, request):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless.new")
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        base_url = ConfigReader.get_base_url()
        self.driver.get(base_url)   
        sleep(5)
        request.cls.driver = self.driver
        
    
        
        
        yield
        self.driver.quit()
    # end def