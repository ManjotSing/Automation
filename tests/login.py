from selenium import webdriver
from config.factory_manager import FactoryManager
import time
import unittest
from pages.home_page import HomePage
from pages.login_page import LoginPage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = FactoryManager.createDriver('Chrome');

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

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed.')

    if __name__=='__main__':
        unittest.main()