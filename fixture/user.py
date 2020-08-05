from selenium.webdriver.common.by import By
from model.user import User


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
        self.return_home_page()
        self.user_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def return_home_page(self):
        wd = self.app.wd
        # return Home page
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home page").click()

    def select_element_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_user_by_index(self, index, new_user_data):
        wd = self.app.wd
        # click add new contact
        self.open_home_page()
        self.select_element_by_index(index)
        # edit user
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.edit_userInfo(new_user_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        # return Home page
        self.return_home_page()
        self.user_cache = None

    def edit_first_user(self, contact):
        wd = self.app.wd
        self.edit_user_by_index(0, contact)

    def delete_user_by_index(self, index):
        wd = self.app.wd
        # click add new contact
        self.open_home_page()
        self.select_element_by_index(index)
        wd.find_element(By.XPATH, "//input[@value=\'Delete\']").click()
        assert wd.switch_to.alert.text == "Delete 1 addresses?"
        wd.switch_to.alert.accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.open_home_page()
        self.user_cache = None

    def delete_first_user(self):
        self.delete_user_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.user_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.find_element_by_name("selected[]").get_attribute("title")
                lastname = wd.find_elements_by_tag_name("td")[1]
                firstname = wd.find_elements_by_tag_name("td")[2]
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.user_cache.append(User(name=text, id=id, lastname=lastname, firstname=firstname))
        return list(self.user_cache)

