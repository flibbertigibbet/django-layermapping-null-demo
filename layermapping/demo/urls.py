from django.conf.urls import url
from django.contrib import admin

from demo.views import index

urlpatterns = [
    url(r'^', index, name='index'),
]
