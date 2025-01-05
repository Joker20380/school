import this

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import *

class PersonalAreaForm(UserChangeForm):
    birth = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%d.%m.%Y', attrs={'class':
                                                                                                         'single-input',
                                                                                                     'placeholder': 'Дата рождения'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'first_name',)
