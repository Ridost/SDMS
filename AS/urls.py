from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),  # index as default
    path('login/', views.login),
    path('main/', views.main),
    path('logout/', views.logout),
    path('modify/', views.modify),
    path('modify_password/', views.modify_password),
]