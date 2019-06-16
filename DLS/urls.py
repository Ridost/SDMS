from django.urls import path, re_path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('billboard/', ShowBillboard),
    re_path('billboard/([0-9]+)/$', ShowSpecificBillboard),
    path('billboard/add/', AddBillboard),
    path('billboard/delete/', DeleteBillboard),
    path('billboard/modify/', ModifyBillboard),

    path('package/', ShowPackage),
    path('package/manage/', ManagePackage),
    path('package/verify/', VerifyPackage),


    path('borrow/manage/showall', ShowRecord),
    path('borrow/manage/', ManageRecord),
    path('borrow/manage/confirm/', ConfirmRecord),
    path('borrow/manage/withdraw/', WithdrawRecord),

    path('borrow/apply/', BorrowSpace),
    path('borrow/status/', ShowStatus),
    path('borrow/check/', CheckSpace),
    
]