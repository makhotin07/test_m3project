from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.ui import ModelEditWindow
from .ui import UserAddWindow
from .controller import observer


class UserPack(ObjectPack):

    model = User
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = UserAddWindow
    columns = [
        {
            'data_index': '__unicode__',
            'hidden': True,
        },
        {
            'data_index': 'username',
            'header': u'Username',
        },
        {
            'data_index': 'first_name',
            'header': u'Имя',
        },
        {
            'data_index': 'last_name',
            'header': u'Фамилия',
        },
        {
            'data_index': 'email',
            'header': u'Email',
        },
    ]


class GroupPack(ObjectPack):

    add_window = edit_window = ModelEditWindow.fabricate(model=Group)
    model = Group
    add_to_menu = True
    columns = [
        {
            'data_index': 'name',
            'header': u'Наименование',
        },
        {
            'data_index': 'permissions',
            'header': u'Разрешения',
        },
    ]
    add_to_desktop = True


class ContentTypePack(ObjectPack):

    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)
    model = ContentType
    add_to_menu = True
    add_to_desktop = True


class PermissionPack(ObjectPack):

    add_window = edit_window = ModelEditWindow.fabricate(model=Permission,
                                                         model_register=observer)
    model = Permission
    add_to_menu = True
    add_to_desktop = True
