# Automation

Automation is a selenium based automation project which follows POM design pattern. Page-object-model (POM) is a pattern that you can apply it to develop efficient automation framework. With page-model, it is possible to minimise maintenance cost. Basically page-object means that your every page is inherited from a base class which includes basic functionalities for every pages. If you have some new functionality that every pages have, you can simple add it to the base class.

Pages:
  1. BasePage class include basic functionality and driver initialization
  2. LoginPage class includes loginng user into the application('https://opensource-demo.orangehrmlive.com/').
  3. LeaveDetailsPage class includes the functionality to apply for a leave by filling all the required details.
  4. MyLeavesPage class adds one more layer to this project for MyLeaves option under Leaves tab of menu bar.
  5. SearchLeavesPage class inherits MyleavePage as search functionality comes under MyLeaves tab.
  6. Finally, HomePage class includes functionality of logout the user.

TestCases:
  1. Include basic login and logout.
  2. Include apply a leave by filling all required details.
  3. Include searching a leave within specified date range. 
  
DriverFactory class follows factory pattern to return driver.

Locators class stores list of all locators differentiated by page.

