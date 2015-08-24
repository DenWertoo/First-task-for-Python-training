__author__ = 'chekluev.d'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_name(contact)
        # fill company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # fill address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("theform").click()
        # fill phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        # fill email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # fill date of birth
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[15]").click()
#        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1980")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def fill_contact_name(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
#        wd.find_element_by_name("middlename").click()
#        wd.find_element_by_name("middlename").clear()
#        wd.find_element_by_name("middlename").send_keys(contact.middlename)
#        wd.find_element_by_name("lastname").click()
#        wd.find_element_by_name("lastname").clear()
#        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        #wd.find_element_by_name("title").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact()
        #submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        #wd.find_element_by_link_text("home").click()
        #self.return_to_home_page()

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        #self.select_contact()
        # open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[5]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_name(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()

#    def edit_contact(self, contact):
#        wd = self.app.wd
#        self.open_home_page()
#        #select contact
#        wd.find_element_by_name("selected[]").click()
#        #edit contact
#        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[5]/td[8]/a/img").click()
#        wd.find_element_by_name("firstname").click()
#        wd.find_element_by_name("firstname").clear()
#        wd.find_element_by_name("firstname").send_keys(contact.firstname)
#        wd.find_element_by_name("middlename").click()
#        wd.find_element_by_name("middlename").clear()
#        wd.find_element_by_name("middlename").send_keys(contact.middlename)
#        wd.find_element_by_name("lastname").click()
#        wd.find_element_by_name("lastname").clear()
#        wd.find_element_by_name("lastname").send_keys(contact.middlename)
#        wd.find_element_by_name("company").click()
#        wd.find_element_by_name("company").clear()
#        wd.find_element_by_name("company").send_keys(contact.company)
#        wd.find_element_by_name("address").click()
#        wd.find_element_by_name("address").clear()
#        wd.find_element_by_name("address").send_keys(contact.address)
#        wd.find_element_by_name("home").click()
#        wd.find_element_by_name("home").clear()
#        wd.find_element_by_name("home").send_keys(contact.homephone)
#        wd.find_element_by_name("mobile").click()
#        wd.find_element_by_name("mobile").clear()
#        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
#        wd.find_element_by_name("email").click()
#        wd.find_element_by_name("email").clear()
#        wd.find_element_by_name("email").send_keys(contact.email)
#        wd.find_element_by_name("byear").click()
#        wd.find_element_by_name("byear").clear()
#        wd.find_element_by_name("byear").send_keys("1985")
#        #submit update and return home page
#        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
#        self.return_to_home_page()


    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))