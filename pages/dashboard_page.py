import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from time import sleep
from selenium import webdriver
class DashboardPage():
    DASHBOARD = (By.XPATH,"//h6[text()='Dashboard']")
    
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_displayed(self):
        dashboard = self.driver.find_element(*self.DASHBOARD)
        return dashboard.is_displayed()


