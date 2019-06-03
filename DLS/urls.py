<<<<<<< HEAD
from django.urls import path, re_path
=======
from django.urls import path
>>>>>>> 4b7e473f7b61da3759f131302d136c6d6d6c80f4
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('billboard', ShowBillboard),
    path('addbillboard', AddBillboard),
    path('deletebillboard', DeleteBillboard),
    path('modifybillboard', ModifyBillboard),
<<<<<<< HEAD

    path('package', ShowPackage),
    path('package/manage', ManagePackage),
    path('package/verify', VerifyPackage),
    re_path(r'^package/modify/?([0-9]*)/$', ModifyPackage),
    path('package/delete', DeletePackage),
=======
    path('package', ShowPackage)
>>>>>>> 4b7e473f7b61da3759f131302d136c6d6d6c80f4
]