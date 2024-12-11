import os
import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from mdeditor.fields import MDTextField
from .fields import WEBPField


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Раздел сайта", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'section_slug': self.slug})

    class Meta:
        verbose_name = 'Раздел сайта'
        verbose_name_plural = 'Разделы сайта'
        ordering = ['id']


class CategoryProg(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория програмы'
        verbose_name_plural = 'Категории программ'
        ordering = ['id']


class Prog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", null=True, blank=True)
    content = MDTextField(blank=True, verbose_name="Содержание")
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото2", null=True, blank=True)
    selection_procedure = MDTextField(blank=True, null=True, verbose_name="Порядок отбора")
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото3", null=True, blank=True)
    selection_procedure2 = MDTextField(blank=True, null=True, verbose_name="Порядок отбора 2 абзац")
    photo4 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото4", null=True, blank=True)
    prog_statement = MDTextField(blank=True, verbose_name="Положение о программе")
    photo5 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото5", null=True, blank=True)
    prog_statement2 = MDTextField(blank=True, verbose_name="Положение о программе 2 абзац")
    name_pdffile = models.CharField(max_length=255, verbose_name="Имя PDF файла", null=True, blank=True)
    pdffile = models.FileField(upload_to="pdf/%Y/%m/%d/", verbose_name="PDF", null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    time_start = models.DateTimeField(verbose_name="Дата и время начала программы", null=True, blank=True)
    time_ending = models.DateTimeField(verbose_name="Дата и время окончания программы", null=True, blank=True)
    is_published = models.BooleanField(verbose_name="Публикация")
    supervisor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='supervisor', verbose_name="Руководитель",
                                   null=True, blank=True)
    registration = models.ManyToManyField(User, related_name="progs", verbose_name="Участники программы", blank=True)
    cat = models.ForeignKey(CategoryProg, on_delete=models.PROTECT, verbose_name="Категория", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('program', kwargs={'program_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'
        ordering = ['time_create', 'title']


class CategoryLecture(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_lecture', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория лекции'
        verbose_name_plural = 'Категории лекций'
        ordering = ['id']


class Lecture(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    URL = models.URLField(blank=True, verbose_name="Ссылка на видео")
    prog = models.ForeignKey("Prog", on_delete=models.PROTECT, verbose_name="Программа", blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey(CategoryLecture, on_delete=models.PROTECT, verbose_name="Категория", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lecture', kwargs={'lecture_slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Лекции'
        verbose_name_plural = 'Лекции'
        ordering = ['time_create', 'title']


class Documents(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = MDTextField(blank=True, verbose_name="Содержание")
    name_pdffile = models.CharField(max_length=255, verbose_name="Имя PDF файла", null=True, blank=True)
    doc_file = models.FileField(upload_to="pdf/%Y/%m/%d/", verbose_name="Файл", null=True, blank=True)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name="Исполнитель")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    section = models.ManyToManyField(Section, related_name="Документы", verbose_name="Раздел сайта", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('doc', kwargs={'doc_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['time_create']


class CategoryNews(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'
        ordering = ['id']

def image_folder(instance, filename):
    return 'photos/{}.webp'.format(uuid.uuid4().hex)


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = MDTextField(blank=True, verbose_name="Текст")
    photo = WEBPField(verbose_name='фото 633x550px', upload_to=image_folder, blank=True, null=True)
    photo2 = WEBPField(verbose_name='фото2', upload_to=image_folder,  blank=True, null=True)
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото№3", blank=True, null=True)
    photo4 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото№4", blank=True, null=True)
    photo5 = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото№5", blank=True, null=True)
    time_create = models.DateTimeField(verbose_name="Дата и время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey(CategoryNews, on_delete=models.PROTECT, verbose_name="Категория")
    prog = models.ForeignKey('Prog', on_delete=models.PROTECT, verbose_name="Программа", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['time_create', 'title']

