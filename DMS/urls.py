from django.urls import path
from DMS import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('main/',views.DMS, name = 'main'),
    path('DormitoryApply/', views.DormitoryApply),
    path('DormCheck/', views.DormCheck),
    path('DormDelete/', views.DormDelete),
]