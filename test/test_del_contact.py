from model.user import User
from random import randrange


def test_delete_user(app):
    if app.user.count() == 0:
        app.user.create_user(User(firstname = "user_for_delete"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    assert len(old_users) - 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users[index:index+1] = []
    assert sorted(old_users, key = User.id_or_max) == sorted(new_users, key = User.id_or_max)
