from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def click_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home page").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        # click add new contact
        self.app.open_home_page()
        self.click_add_new_contact()
        self.fill_contact_form(contact)
        self.submit()
        # return to home page
        self.return_home_page()
        self.contact_list = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)

    def select_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_element_by_index(index)
        # press Delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.contact_list = None

    def click_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        # click add new contact
        self.app.open_home_page()
        self.select_element_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        self.update_changes()
        # return to home page
        self.return_home_page()
        self.contact_list = None

    def select_element_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def update_changes(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def count(self):
        wd = self.app.wd
        self.click_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_list = None

    def get_contact_list(self):
        if self.contact_list is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_list = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_list.append(Contact(id = id, firstname = firstname, lastname = lastname,
                                                 all_phones_from_home_page = all_phones, address = address,
                                                 email = all_email))
        return list(self.contact_list)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname = firstname, lastname = lastname, id = id, address = address, home = home,
                       mobile = mobile, phone2 = phone2, work = work,
                       email = email, email2 = email2, email3 = email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work,
                       mobile=mobile, phone2=phone2)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def add_contact_to_group(self, group_id, id):
        wd = self.app.wd
        self.select_element_by_index(id)
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("home").click()

    def delete_contact_from_group(self, value, id):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_value(value)
        self.select_element_by_index(id)
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_value("")
