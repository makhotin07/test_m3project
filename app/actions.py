from datetime import datetime, date

from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from m3 import ApplicationLogicException
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from app import ui


class PersonPack(ObjectPack):
    model = User
    add_window = ui.PersonAddWindow
    # разрешим добавлять ссылку на list_window в меню Desktop'а
    add_to_menu = True
    can_delete = True

    def save_row(self, obj, create_new, request, context):
        # if not (obj.username.isalpha() and obj.last_name.isalpha()):
        #     raise ApplicationLogicException(
        #         u'Имя и Фамилимя могут содержать только буквы алфавита!')
        super(PersonPack, self).save_row(obj, create_new, request, context)

    def delete_row(self, obj_id, request, context):
        if date.today().weekday() in (5, 6):
            raise ApplicationLogicException(
                u'Нельзя удалять записи в выходные дни!')

        # не хотим использовать m3.db.safe_delete
        obj = self.model.objects.get(id=obj_id)
        obj.delete()
        return obj


class PermissionPack(ObjectPack):
    model = Permission
    add_window = edit_window = ModelEditWindow.fabricate(model)

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    add_to_menu = True


class GroupPack(ObjectPack):
    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model)

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    add_to_menu = True


class ContentTypePack(ObjectPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model)

    # разрешим добавлять ссылку на list_window в меню Desktop'а
    add_to_menu = True

    def save_row(self, obj, create_new, request, context):
        if not (obj.name.isalpha() and obj.surname.isalpha()):
            raise ApplicationLogicException(
                u'Имя и Фамилимя могут содержать только буквы алфавита!')
        super(PersonPack, self).save_row(obj, create_new, request, context)
