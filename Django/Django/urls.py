
from django.contrib import admin
from django.urls import path, include

from INSTALLED_APPS.views import test

urlpatterns = [
    path('',test),
    path('admin/', admin.site.urls),
    path('news/', include('News.urls')),
    ]
