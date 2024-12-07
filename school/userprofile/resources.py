from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import *


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'userprofile__patronymic', )


class UserResource2(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name',)