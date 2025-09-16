import pytest
from selenium.webdriver.common.by import By
from automation_framework.pages.login_page import LoginPage
from time import sleep
from selenium import webdriver
from base.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD = (By.XPATH,"//h6[text()='Dashboard']")
    
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_displayed(self):
        dashboard = self.driver.find_element(*self.DASHBOARD)
        return dashboard.is_displayed()


