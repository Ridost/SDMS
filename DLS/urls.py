from django.urls import path, re_path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('billboard', ShowBillboard),
    path('addbillboard', AddBillboard),
    path('deletebillboard', DeleteBillboard),
    path('modifybillboard', ModifyBillboard),

    path('package', ShowPackage),
    path('packagemanage', ManagePackage),
    path('verifypackage', VerifyPackage),
    re_path(r'^modifypackage/?([0-9]*)/$', ModifyPackage),
    path('deletepackage', DeletePackage),
]