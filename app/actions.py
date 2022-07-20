from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .models import User


class UserPack(ObjectPack):

    model = User

    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_menu = True

    columns = [
        {
            "data_index": "username",
            "header": u"Имя пользователя",
            "width": 2,
        },
        {
            "data_index": "first_name",
            "header": u"Имя",
            "width": 2,
        },
        {
            "data_index": "last_name",
            "header": u"Фамилия",
            "width": 2,
        },
        {
            "data_index": "email",
            "header": u"Электронный адрес",
            "width": 2,
        },
        {
            "data_index": "groups",
            "header": u"Группа",
            "width": 2,
        },
        {
            "data_index": "user_permissions",
            "header": u"Права",
            "width": 2,
        },
        {
            "data_index": "is_staff",
            "header": u"Администратор",
            "width": 1,
        },
        {
            "data_index": "last_login",
            "header": u"Был последний раз",
            "width": 1,
        },
        {
            "data_index": "date_joined",
            "header": u"Аккаунт создан",
            "width": 1,
        },
    ]
