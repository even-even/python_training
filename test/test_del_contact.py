from model.user import User


def test_delete_user(app):
    if app.user.count() == 0:
        app.user.create_user(User(firstname = "user_for_delete"))
    app.user.delete_first_user()
