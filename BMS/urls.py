from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('stuinfo_import/', views.stuinfo_import),
    path('mail_import/', views.mail_import),
]