from model.group import Group
from random import randrange


def test_delete_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name = "group_for_delete"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
    if check_ui:
        new_groups = app.group.get_group_list()
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
