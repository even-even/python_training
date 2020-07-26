class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # open group page
        wd.find_element_by_link_text("groups").click()
        # input group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.edit_groupInfo(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_groupInfo(self, group):
        """ edit Info about group.
        Use in create and edit groupInfo"""
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd

        self.open_group_page()

        self.select_first_group()
        wd.find_element_by_name("edit").click()

        self.edit_groupInfo(new_group_data)
        wd.find_element_by_name("update").click()

        # return to group page
        wd.find_element_by_link_text("group page").click()
