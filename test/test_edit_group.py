__author__ = 'chekluev.d'
from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="asd", header="asf", footer="asg"))
    app.session.logout()