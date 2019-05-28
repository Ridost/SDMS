from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('test', views.current_datetime, name='current_datetime'),
]