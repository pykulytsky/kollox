import pytest
from authentication.user import UserCreator

pytestmark = [pytest.mark.django_db]


def test_base_user_creator(user):
    user_creator = UserCreator(username=user.username,
                               email=user.email,
                               password=user.password)

    assert user.username == user_creator.username
    assert user.email == user_creator.email
    assert user.password == user_creator.password


def test_user_creator_with_already_taken_user_credentials(user):
    user_creator = UserCreator(username=user.username,
                               email=user.email,
                               password=user.password)

    new_user = user_creator.create()

    assert user == new_user[0]


def test_user_creator_just_update_field(user):
    user_creator = UserCreator(username=user.username,
                               email=user.email,
                               password=user.password)

    new_user = user_creator.create()

    assert new_user[1] is not True


def test_user_creator_create_new_user():
    user_creator = UserCreator(username="new_user",
                               email="test1@py.com",
                               password="123456")

    new_user = user_creator.create()

    assert new_user[1]


def test_new_user_by_user_creator():
    user_creator = UserCreator(username="new_user",
                               email="test1@py.com",
                               password="123456")

    new_user = user_creator.create()[0]

    assert new_user.username == 'new_user'
    assert new_user.email == 'test1@py.com'
    assert new_user.password == '123456'


def test_user_creator_user_property():
    user_creator = UserCreator(username="new_user",
                               email="test1@py.com",
                               password="123456")

    new_user = user_creator.create()

    assert user_creator.user.username == 'new_user'
    assert user_creator.user.email == 'test1@py.com'
    assert user_creator.user.password == '123456'
    assert new_user[0].username == 'new_user'
