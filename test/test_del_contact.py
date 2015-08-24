__author__ = 'chekluev.d'
from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Tip", middlename="Tip", lastname="Tipy", company="ladCompany", address="Ca, adventure", homephone="+7098", mobilephone="+75325623895",
                            email="tip.tipytip.@ladcompany.ru"))
    app.contact.delete_contact()