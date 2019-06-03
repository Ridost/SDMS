from django.urls import path
from DMS import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('DMS',views.DMS, name = 'DMS'),
    path('DormitoryApply', views.DormitoryApply),
    path('DormCheck', views.DormCheck),
    path('DormDelete', views.DormDelete),
    path('DormInfo', views.DormInfoCreate),
]