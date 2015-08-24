__author__ = 'chekluev.d'

from model.contact import Contact

def test_modify_firstname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tip", middlename="Tip", lastname="Tipy", company="ladCompany", address="Ca, adventure", homephone="+7098", mobilephone="+75325623895",
                            email="tip.tipytip.@ladcompany.ru"))
    app.contact.modify_contact(Contact(firstname="New firstname"))

def test_modify_middlename_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tip", middlename="Tip", lastname="Tipy", company="ladCompany", address="Ca, adventure", homephone="+7098", mobilephone="+75325623895",
                            email="tip.tipytip.@ladcompany.ru"))
    app.contact.modify_contact(Contact(middlename="New middlename"))

def test_modify_lastname_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tip", middlename="Tip", lastname="Tipy", company="ladCompany", address="Ca, adventure", homephone="+7098", mobilephone="+75325623895",
                            email="tip.tipytip.@ladcompany.ru"))
    app.contact.modify_contact(Contact(lastname="New lastname"))
