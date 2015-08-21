# -*- coding: utf-8 -*-
from model.group import Group


def test_group_creation(app):
    app.group.create(Group(name="F1", header="F2", footer="F3"))

def test_empty_group_creation(app):
    app.group.create(Group(name="", header="", footer=""))