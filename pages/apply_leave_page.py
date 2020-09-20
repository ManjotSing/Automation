from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import HomeLocators
from locators.locators import LeaveLocators
class LeaveDetailPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver);

    def click_apply_leave(self):
        self.driver.find_element(By.XPATH, LeaveLocators.menu_leave_tab).click();

    def select_leave_type(self,leavetype):
        self.driver.find_element(By.XPATH, LeaveLocators.select_leave_type).click();
        if leavetype=='Vacation US':
            self.driver.find_element(By.XPATH, LeaveLocators.leave_type_vacation).click();
        elif leavetype=='FMLA US':
            self.driver.find_element(By.XPATH, LeaveLocators.leave_type_fmla).click();

    def leave_from_date(self,fromdate):
        self.driver.find_element(By.XPATH,LeaveLocators.leave_from_date).clear();
        self.driver.find_element(By.XPATH, LeaveLocators.leave_from_date).send_keys(fromdate);

    def leave_to_date(self,todate):
        self.driver.find_element(By.XPATH,LeaveLocators.leave_to_date).clear();
        self.driver.find_element(By.XPATH, LeaveLocators.leave_to_date).send_keys(todate);

    def apply_leave(self):
        self.driver.find_element(By.ID,LeaveLocators.button_leave_apply).click();
        self.driver.implicitly_wait(30);
