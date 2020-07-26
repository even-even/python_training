from model.group import Group


def test_edit_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.edit_first_group(Group(name = "editName", header = "editHeader", footer = "editFooter"))
    app.session.logout()