from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('test/', views.current_datetime),
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    #path('sign/', views.sign),
]