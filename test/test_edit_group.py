from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "group_for_edit"))
    app.group.edit_first_group(Group(name = "editName", header = "editHeader", footer = "editFooter"))
