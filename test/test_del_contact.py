__author__ = 'chekluev.d'
from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testname"))
    app.contact.delete_contact()