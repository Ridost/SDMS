from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('test', views.current_datetime, name='current_datetime'),
<<<<<<< HEAD
    path('login', views.login, name='login'),
    #path('index', views.index, name='index')

=======
>>>>>>> 4ef92db0eef10847a2a5ca012e551d1494c2a5c3
]