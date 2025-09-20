import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from base.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestVacancies(BaseTest):

    def test_add_vacancy(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Recruitment"))
        )

        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.add_vacancy("Test Vacancy Name")


