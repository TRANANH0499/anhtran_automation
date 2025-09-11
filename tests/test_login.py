import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from time import sleep
from pages.dashboard_page import DashboardPage

class TestLogin(BaseTest):
    
    def test_login_valid(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("Admin", "admin123")
        
        dashboardpage = DashboardPage(self.driver)
        assert dashboardpage.is_dashboard_displayed() is True
        sleep(5)

        
