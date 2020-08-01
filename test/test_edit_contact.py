from model.user import User


def test_edit_user(app):
    if app.user.count() == 0:
        app.user.create_user(User(firstname = "user_for_edit"))
    old_users = app.user.get_user_list()
    user = User(firstname = "edit1", middlename = "edit2", lastname = "edit3", nickname = "edit4", title = "edit5",
                company = "edit6", address = "edit7", home = "edit8", mobile = "edit9", work = "edit10", fax = "edit11",
                email = "edit12", email2 = "edit13", email3 = "edit14", homepage = "edit15", address2 = "edit16",
                phone2 = "edit17", notes = "edit18")
    user.id = old_users[0].id
    app.user.edit_user(user)
    new_users = app.user.get_user_list()
    assert len(old_users) == app.user.count()
    old_users[0] = user
    assert sorted(old_users, key=User.id_or_max) == sorted(new_users, key=User.id_or_max)
