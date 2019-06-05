from django.urls import path
from DMS import views

urlpatterns = [
    path('main/',views.main, name = 'main'),
    path('DormitoryApply/', views.DormitoryApply),
    path('DormCheck/', views.DormCheck),
    path('DormDelete/', views.DormDelete),
    #path('DormDistribution/', views.DormDistribution),
    #path('BillCreate/', views.BillCreate),
]