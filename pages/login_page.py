from locators.locators import *
from pages.base_page import BasePage
class LoginPage(BasePage):

    def __init__(self,driver):
        self.locator = LoginLocators
        super().__init__(driver);


    def enter_user_name(self,username):
        self.driver.find_element_by_id(self.locator.username_id).clear()
        self.driver.find_element_by_id(self.locator.username_id).send_keys(username);

    def enter_user_password(self, password):
        self.driver.find_element_by_id(self.locator.password_id).clear()
        self.driver.find_element_by_id(self.locator.password_id).send_keys(password);

    def login(self):
        self.driver.find_element_by_id(self.locator.login_button).click();