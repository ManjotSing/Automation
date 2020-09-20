from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.locators import LeaveLocators
class MyLeavesPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver);

    def open_myleaves(self):
        self.driver.find_element(By.XPATH,LeaveLocators.menu_my_leaves).click();
