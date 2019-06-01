from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('billboard', ShowBillboard),
    path('addbillboard', AddBillboard),
    path('deletebillboard', DeleteBillboard),
    path('modifybillboard', ModifyBillboard),
    path('package', ShowPackage),
    path('packagemanage', ManagePackage)
]