import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from time import sleep

class TestLogin(BaseTest):
    def test_login_valid(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("Admin", "admin123")
        sleep(5)

        
