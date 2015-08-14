# -*- coding: utf-8 -*-
from model.group import Group


def test_group_creation(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="F1", header="F2", footer="F3"))
    app.session.logout()

def test_empty_group_creation(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()