from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from mdeditor.fields import MDTextField


class SchoolClass(models.Model):
    school_class = models.CharField(max_length=10, null=True, blank=True, verbose_name="Учебный класс")

    def __str__(self):
        return self.school_class

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class School(models.Model):
    school = models.CharField(max_length=100, null=True, blank=True, verbose_name="Школа")

    def __str__(self):
        return self.school

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class District(models.Model):
    district = models.CharField(max_length=100, null=True, blank=True, verbose_name="Муниципалитет")

    def __str__(self):
        return self.district

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True, verbose_name="Отчество")
    birth = models.DateTimeField(null=True, blank=True, verbose_name="Дата рождения")
    school_class = models.ForeignKey(SchoolClass, on_delete=models.PROTECT, verbose_name="Класс", null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.PROTECT, verbose_name="Школа", null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Муниципалитет", null=True, blank=True)
    merit = MDTextField(blank=True, verbose_name="Заслуги", null=True)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
