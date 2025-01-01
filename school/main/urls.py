from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *


urlpatterns = [
                path('', Index.as_view(), name='index'),
                path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
                path('about/', About.as_view(), name='about'),

    ]