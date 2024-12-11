from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from .models import *
#from .resources import *


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class CategoryNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class NewsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#    resource_classes = [ArticleResource]
    list_display = ('id', 'title', 'get_photo', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'


class CategoryLectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


class CategoryProgAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class ProgAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#    resource_classes = [ProgResource, ProgResource2]
    list_display = ('id', 'title', 'get_photo', 'supervisor', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    filter_horizontal = ('registration',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Фото'


class DocumentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #resource_classes = [HomeWorkResource]
    list_display = ('id', 'title', 'name_pdffile', 'is_published')
    list_display_links = ('id', 'title', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Section, SectionAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(CategoryNews, CategoryNewsAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(CategoryLecture, CategoryLectureAdmin)
admin.site.register(Prog, ProgAdmin)
admin.site.register(CategoryProg, CategoryProgAdmin)
admin.site.register(Documents, DocumentsAdmin)

admin.site.site_title = 'Администрирование сайта'
admin.site.site_header = 'Администрирование сайта'

