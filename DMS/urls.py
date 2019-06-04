from django.urls import path
from DMS import views

urlpatterns = [
    path('main/',views.DMS, name = 'main'),
    path('DormitoryApply/', views.DormitoryApply),
    path('DormCheck/', views.DormCheck),
    path('DormDelete/', views.DormDelete),
    path('DormRecordCreate', views.DormRecordCreate),
]