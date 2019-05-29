from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
import datetime

#from AS.model import DormiotoryApply
# Create your views here.


def hello(request):
    message = "Hello World!!"
    return render(request,"DMS/hello.html",locals())

def DMS(request):
    return render(request,"DMS/DMS.html",locals())

def DormitoryApply(request):
    start = settings.STARTTIME
    end = settings.ENDTIME
    now = datetime.datetime.now()
    if now>start and now<end:
        message = "有效"
    else:
        message = "無效"
    return render(request,"DMS/DormitoryApply.html",locals())
