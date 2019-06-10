from django.urls import path, re_path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('billboard', ShowBillboard),
    path('addbillboard', AddBillboard),
    path('deletebillboard', DeleteBillboard),
    path('modifybillboard', ModifyBillboard),

    path('package', ShowPackage),
    path('package/manage', ManagePackage),
    path('package/verify', VerifyPackage),
    re_path(r'^package/modify/?([0-9]*)/$', ModifyPackage),
    path('package/delete', DeletePackage),

    path('borrow', BorrowSpace),
    path('borrow/check', CheckSpace)
]