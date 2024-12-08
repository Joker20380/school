from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *


urlpatterns = [
                path('', Index.as_view(), name='index'),

    ]