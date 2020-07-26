from selenium.webdriver.common.by import By


class UserHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_userInfo(self, user):
        """ edit Info about user.
        Use in create and edit userInfo"""

        wd = self.app.wd
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("middlename", user.middlename)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("nickname", user.nickname)
        self.change_field_value("title", user.title)
        self.change_field_value("company", user.company)
        self.change_field_value("address", user.address)
        self.change_field_value("home", user.home)
        self.change_field_value("mobile", user.mobile)
        self.change_field_value("work", user.work)
        self.change_field_value("fax", user.fax)
        self.change_field_value("email", user.email)
        self.change_field_value("email2", user.email2)
        self.change_field_value("email3", user.email3)
        self.change_field_value("homepage", user.homepage)
        self.change_field_value("address2", user.address2)
        self.change_field_value("phone2", user.phone2)
        self.change_field_value("notes", user.notes)

    def create_user(self, user):
        wd = self.app.wd
        # click Add new
        wd.find_element_by_link_text("add new").click()
        self.edit_userInfo(user)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return Home page
        wd.find_element_by_link_text("home page").click()

    def edit_user(self, new_user_data):
        wd = self.app.wd

        # click home
        wd.find_element_by_link_text("home").click()

        # edit user
        wd.find_element(By.XPATH, "//img[@alt=\'Edit\']").click()
        self.edit_userInfo(new_user_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        # return Home page
        wd.find_element_by_link_text("home page").click()

    def delete_user(self):
        wd = self.app.wd

        # click home
        wd.find_element_by_link_text("home").click()
        # check 1st element and delete it
        wd.find_element_by_name("selected[]").click()
        wd.find_element(By.XPATH, "//input[@value=\'Delete\']").click()
        assert wd.switch_to.alert.text == "Delete 1 addresses?"
        wd.switch_to.alert.accept()

        wd.find_element(By.LINK_TEXT, "home").click()
