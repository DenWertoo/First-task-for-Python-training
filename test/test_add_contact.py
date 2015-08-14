# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from fixture.contact_application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username = "admin", password = "secret")
    app.add_contact(Contact(firstname = "Tip", middlename = "Tip", lastname = "Tipy", company = "ladCompany", address = "Ca, adventure", homephone = "+7098", mobilephone = "+75325623895",
                         email = "tip.tipytip.@ladcompany.ru"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username = "admin", password = "secret")
    app.add_contact(Contact(firstname = "", middlename = "", lastname = "", company = "", address = "", homephone = "", mobilephone = "",
                         email = ""))
    app.logout()
