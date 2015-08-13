# -*- coding: utf-8 -*-
import pytest

from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_group_creation(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="F1", header="F2", footer="F3"))
    app.logout()

def test_empty_group_creation(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()