from django.urls import path
from RS import views

urlpatterns =[
    path('index/',views.index),
    path('RepairmentApply',views.RepairmentApply),
    path('ReportApply',views.ReportApply),
]