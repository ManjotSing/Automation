from config.factory_manager import DriverFactory
import time
import unittest
from locators.locators import HomeLocators
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.apply_leave_page import LeaveDetailPage
from pages.search_leaves import SearchLeaves

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.create_driver('Chrome');

    def test_login_valid(self):
        driver= self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver);
        login.enter_user_name("Admin");
        login.enter_user_password('admin123')
        login.login()

        home = HomePage(driver);
        home.welcome_click();
        home.logout_click();
        time.sleep(4)

    def test_apply_leave(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver);
        login.enter_user_name("Admin");
        login.enter_user_password('admin123')
        login.login()

        home = HomePage(driver);

        leave = LeaveDetailPage(driver);
        leave.hover(HomeLocators.leave_hover);
        leave.click_apply_leave();
        leave.select_leave_type('Vacation US');
        leave.leave_from_date('2020-09-29');
        leave.leave_to_date('2020-09-29');
        leave.apply_leave();

        home.welcome_click();
        home.logout_click();
        time.sleep(4)

    def test_my_leaves(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver);
        login.enter_user_name("Admin");
        login.enter_user_password('admin123')
        login.login()

        home = HomePage(driver);

        searchleave = SearchLeaves(driver);
        searchleave.hover(HomeLocators.leave_hover)
        searchleave.open_myleaves();
        searchleave.from_date('2020-01-01');
        searchleave.to_date('2020-09-29');
        searchleave.search();

        home.welcome_click();
        home.logout_click();
        time.sleep(4)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed.')

    if __name__=='__main__':
        unittest.main()