__author__ = 'chekluev.d'
from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname = "1", middlename = "2", lastname = "3", company = "4", address = "5", homephone = "8902395", mobilephone = "+723098502",
                            email = "feffef@fefef.ru"))
    app.session.logout()