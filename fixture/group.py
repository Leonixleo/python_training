class GroupHelper:

    def __init__(self,app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.chage_fild_value("group_name", group.name)
        self.chage_fild_value("group_header", group.header)
        self.chage_fild_value("group_footer", group.footer)

    def chage_fild_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_ferst_group()
        # Submit first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def select_ferst_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_ferst_group()
        # Edit group
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Обновили название группы ")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("Обновили хедер группы")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("Обновили футер группы")
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def modify_first_group(self, new_group_date):
        wd = self.app.wd
        self.open_groups_page()
        self.select_ferst_group()
        # opem modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_date)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def open_groups_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("new")) > 0:
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

