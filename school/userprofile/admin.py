from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import UserProfile

from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin

from .resources import *
from .models import *


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'school',)
    search_fields = ('school',)
    list_filter = ('school',)


class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_class',)
    search_fields = ('school_class',)
    list_filter = ('school_class',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'district',)
    search_fields = ('district',)
    list_filter = ('district',)


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(ImportExportModelAdmin, UserAdmin, admin.ModelAdmin):
    inlines = (UserInline,)
    resource_classes = [UserResource]
    list_display = ('id', 'username', 'last_name', 'first_name', 'get_patronymic', 'get_image', 'email',)
    search_fields = ('id', 'username', 'last_name', 'first_name', 'get_patronymic', 'school_class', 'school', 'get_image',
                     'email', 'phone_number', 'address')
    list_editable = ('email',)
    list_filter = ('username', 'email')

    def get_patronymic(self, obj):
        return obj.userprofile.patronymic

    def get_image(self, obj):
        if obj.userprofile.image:
            return mark_safe(f"<img src='{obj.userprofile.image.url}' width=50>")

    get_image.short_description = 'Фото'
    get_patronymic.short_description = 'Отчество'


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(District, DistrictAdmin)