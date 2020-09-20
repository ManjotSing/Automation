class LoginLocators():

    #Login Page Objects
    username_id = "txtUsername"
    password_id = "txtPassword"
    login_button = "btnLogin"

class HomeLocators():
    # Home Page Objects
    welcome_link = "welcome";
    logout_link = "Logout";
    leave_hover="menu_leave_viewLeaveModule";

class LeaveLocators():
    menu_leave_tab = "// a[ @ id = 'menu_leave_applyLeave']";

    select_leave_type= "//select[@id='applyleave_txtLeaveType']"
    leave_type_vacation= "//select[@id='applyleave_txtLeaveType']//option[contains(text(),'Vacation US')]"
    leave_type_fmla="//select[@id='applyleave_txtLeaveType']//option[contains(text(),'FMLA US')]";
    leave_from_date="//input[@id='applyleave_txtFromDate']"
    leave_to_date="//input[@id='applyleave_txtToDate']"
    button_leave_apply="applyBtn";

    menu_my_leaves="//a[@id='menu_leave_viewMyLeaveList']"
    search_from_date="calFromDate";
    search_to_date="calToDate";
    button_search_class="plainbtn";