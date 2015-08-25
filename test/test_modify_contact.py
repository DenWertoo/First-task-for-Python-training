__author__ = 'chekluev.d'

from model.contact import Contact

def test_modify_firstname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact(Contact(firstname="New firstname"))

def test_modify_middlename_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact(Contact(middlename="New middlename"))

def test_modify_lastname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact(Contact(lastname="New lastname"))

def test_modify_company_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact(Contact(company="NewCompany"))

def test_modify_address_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact(Contact(address="New address"))

def test_modify_homephone_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact(Contact(homephone="093258"))

def test_modify_mobilephone_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact(Contact(mobilephone="002359"))

def test_modify_email_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact(Contact(email="email@NewCompany.ru"))