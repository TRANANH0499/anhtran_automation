import pytest
from automation_framework.pages.login_page import LoginPage
from automation_framework.pages.recruitment_page import RecruitmentPage
from automation_framework.base.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestVacancies(BaseTest):

    def test_add_vacancy(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.add_vacancy(
            vacancy_name="QC",
            job_title="Account Assistant",
            hiring_manager="John Smith"
        )
