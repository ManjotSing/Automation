from selenium import webdriver
class DriverFactory():

    @staticmethod
    def create_driver(drivertype):
        if drivertype == 'Edge':
            driver = webdriver.Edge(executable_path="../drivers/msedgedriver");
        elif drivertype=='Firefox':
            driver = webdriver.Firefox(executable_path="../drivers/");
        else:
            driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        driver.set_page_load_timeout(120);
        driver.maximize_window();
        driver.implicitly_wait(60);
        return driver