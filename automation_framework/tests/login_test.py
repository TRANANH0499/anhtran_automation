from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(BaseTest):
    
    def test_log(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("Admin", "admin123")
        
        dashboardpage = DashboardPage(self.driver)
        assert dashboardpage.is_dashboard_displayed() is True

        