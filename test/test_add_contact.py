# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    app.user.create_user(
        User(firstname = "1", middlename = "2", lastname = "3", nickname = "4", title = "5", company = "6",
             address = "7", home = "8", mobile = "9", work = "10", fax = "11", email = "12", email2 = "13",
             email3 = "14", homepage = "15", address2 = "16", phone2 = "17", notes = "18"))


def test_add_user_empthy(app):
    app.user.create_user(User(firstname = "", middlename = "", lastname = "", nickname = "", title = "", company = "",
                              address = "", home = "", mobile = "", work = "", fax = "", email = "", email2 = "",
                              email3 = "", homepage = "", address2 = "", phone2 = "", notes = ""))
