from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
class BasePage(object):

    def __init__(self, driver, base_url='https://opensource-demo.orangehrmlive.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element_by_id(*locator)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        self.driver.implicitly_wait(10);

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()