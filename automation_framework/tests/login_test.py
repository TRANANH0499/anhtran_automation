from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
class TestLogin(BaseTest):
    
    def test_log(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("Admin", "admin123")
        
        dashboardpage = DashboardPage(self.driver)
        assert dashboardpage.is_dashboardpage_displayes () is True
        