from locators.locators import *
from pages.base_page import BasePage
class HomePage(BasePage):

    def __init__(self,driver):
        self.locator = HomeLocators
        super().__init__(driver);

    def welcome_click(self):
        self.driver.find_element_by_id(self.locator.welcome_link).click();

    def performance_hover(self):
        self.hover(self.locator.performance_hover);

    def logout_click(self):
        self.driver.find_element_by_link_text(self.locator.logout_link).click();