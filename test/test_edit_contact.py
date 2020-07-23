from model.user import User


def test_edit_user(app):
    app.session.login(username = "admin", password = "secret")
    app.user.edit_user(User(firstname = "edit1", middlename = "edit2", lastname = "edit3", nickname = "edit4",
                            title = "edit5", company = "edit6", address = "edit7", home = "edit8", mobile = "edit9",
                            work = "edit10", fax = "edit11", email = "edit12", email2 = "edit13", email3 = "edit14",
                            homepage = "edit15", address2 = "edit16", phone2 = "edit17", notes = "edit18"))
    app.session.logout()
