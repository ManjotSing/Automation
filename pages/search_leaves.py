from selenium.webdriver.common.by import By

from pages.my_leaves_page import MyLeavesPage
from locators.locators import LeaveLocators
class SearchLeaves(MyLeavesPage):

    def __init__(self,driver):
        super().__init__(driver);

    def from_date(self,from_date):
        self.driver.find_element(By.ID,LeaveLocators.search_from_date).send_keys(from_date);

    def to_date(self,to_date):
        self.driver.find_element(By.ID,LeaveLocators.search_to_date).send_keys(to_date);

    def search(self):
        self.driver.find_element(By.CLASS_NAME,LeaveLocators.button_search_class).click();