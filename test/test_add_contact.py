# -*- coding: utf-8 -*-
from model.add_user import User


def test_add_user(app):
    app.session.login(username = "admin", password = "secret")
    app.create_user(User(firstname = "1", middlename = "2", lastname = "3", nickname = "4", title = "5",
                         company = "6", address = "7", home = "8", mobile = "9", work = "10", fax = "11",
                         email = "12", email2 = "13", email3 = "14", homepage = "15", address2 = "16",
                         phone2 = "17", notes = "18"))
    app.session.logout()
