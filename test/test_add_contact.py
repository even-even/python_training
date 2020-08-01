# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    old_users = app.user.get_user_list()
    user = User(firstname = "1", middlename = "2", lastname = "3", nickname = "4", title = "5", company = "6",
                address = "7", home = "8", mobile = "9", work = "10", fax = "11", email = "12", email2 = "13",
                email3 = "14", homepage = "15", address2 = "16", phone2 = "17", notes = "18")
    app.user.create_user(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == app.user.count()
    old_users.append(user)
    assert sorted(old_users, key = User.id_or_max) == sorted(new_users, key = User.id_or_max)


def test_add_user_empthy(app):
    old_users = app.user.get_user_list()
    user = User(firstname = "", middlename = "", lastname = "", nickname = "", title = "", company = "",
                address = "", home = "", mobile = "", work = "", fax = "", email = "", email2 = "", email3 = "",
                homepage = "", address2 = "", phone2 = "", notes = "")
    app.user.create_user(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == app.user.count()
    old_users.append(user)
    assert sorted(old_users, key = User.id_or_max) == sorted(new_users, key = User.id_or_max)
