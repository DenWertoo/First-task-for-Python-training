__author__ = 'chekluev.d'

from model.contact import Contact
from random import randrange


def test_modify_firstname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New", middlename="Tip", lastname="Tipy", company="ladCompany", address="Ca, adventure", homephone="+7098", mobilephone="+75325623895", email="tip.tipytip.@ladcompany.ru")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_middlename_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_contact(Contact(middlename="New middlename"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

def test_modify_lastname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Tip", middlename="Tip", lastname="New", company="ladCompany", address="Ca, adventure", homephone="+7098", mobilephone="+75325623895", email="tip.tipytip.@ladcompany.ru")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_company_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_contact(Contact(company="NewCompany"))

#def test_modify_address_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_contact(Contact(address="New address"))

#def test_modify_homephone_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_contact(Contact(homephone="093258"))

#def test_modify_mobilephone_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_contact(Contact(mobilephone="772359"))

#def test_modify_email_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_contact(Contact(email="email@NewCompany.ru"))