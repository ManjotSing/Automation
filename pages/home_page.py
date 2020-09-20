from locators.locators import HomeLocators
from locators.locators import LeaveLocators
from pages.base_page import BasePage
class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver);

    def welcome_click(self):
        self.driver.find_element_by_id(HomeLocators.welcome_link).click();

    def logout_click(self):
        self.driver.find_element_by_link_text(HomeLocators.logout_link).click();