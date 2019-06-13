from django.urls import path
from DMS import views

urlpatterns = [
    path('main/',views.main, name = 'main'),
    path('DormitoryApply/', views.DormitoryApply),
    path('DormCheck/', views.DormCheck),
    path('DormDelete/', views.DormDelete),
    path('DormRetreat/<str:username>', views.DormRetreat),
    path('DormRetreat/', views.DormRetreat),
    path('DormRetreatApply/',views.DormRetreatApply),
    path('Retreat/',views.Retreat),
    path('DormSetting/', views.DormSetting),
    path('StudentPermission/', views.StudentPermission),
    #path('DormRecordCreate/', views.DormRecordCreate),
    #path('DormDistribution/', views.DormDistribution),
    #path('BillCreate/', views.BillCreate),
]