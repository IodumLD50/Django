
from django.contrib import admin
from django.urls import path

from News.views import index
from INSTALLED_APPS.views import test_1, test_2

urlpatterns = [

    path('', index),
    path('test/', test_1),
    path('test2/', test_2),
]
