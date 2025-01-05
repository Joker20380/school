from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *


urlpatterns = [
                path('', Index.as_view(), name='index'),
                path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
                path('doc/<slug:doc_slug>/', ShowDoc.as_view(), name='doc'),
                path('prog/<int:prog_id>/add_user/', add_user_to_prog, name='add_user_to_prog'),
                path('about/', About.as_view(), name='about'),
                path('personal_area/', personal_area, name='personal_area'),

    ]