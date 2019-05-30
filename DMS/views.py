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
    #判斷是否為管理員
    start = settings.STARTTIME
    end = settings.ENDTIME
    now = datetime.datetime.now()
    if now>start and now<end:   #開放
        #誰申請 哪個系 年級 學號 姓名 哪一棟宿舍 申請時間 審核狀態
        #宿舍房間狀況 eg. OF 5層樓 20個房間 4個人
        return render(request, "DMS/DormitoryApply.html", locals())
    else:   #不開放
        return render(request, "DMS/DMS.html", locals())



