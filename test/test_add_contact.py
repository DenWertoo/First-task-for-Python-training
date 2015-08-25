# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Tip", middlename="Tip", lastname="Tipy", company="ladCompany", address="Ca, adventure", homephone="+7098", mobilephone="+75325623895", email="tip.tipytip.@ladcompany.ru"))

def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", company="", address="", homephone="", mobilephone="", email=""))