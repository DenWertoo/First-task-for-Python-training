__author__ = 'chekluev.d'
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testname"))
    app.group.delete_first_group()
