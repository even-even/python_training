from model.group import Group


def test_edit_group(app):
    app.group.edit_first_group(Group(name = "editName", header = "editHeader", footer = "editFooter"))
