from model.user import User


def test_delete_user(app):
    old_users = app.user.get_user_list()
    user = User(firstname = "user_for_delete")
    if app.user.count() == 0:
        app.user.create_user(User(firstname = "user_for_delete"))
    app.user.delete_first_user()
    assert len(old_users) - 1 == app.user.count()
    new_users = app.user.get_user_list()
    old_users[0:1] = []
    assert sorted(old_users, key = User.id_or_max) == sorted(new_users, key = User.id_or_max)
