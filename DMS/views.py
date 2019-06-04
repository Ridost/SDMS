from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from AS.models import Account,StudentInfo,DormRecord,DormInfo
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime,random

#from AS.model import DormiotoryApply
# Create your views here.


def hello(request):
    message = "Hello World!!"
    return render(request,"DMS/hello.html",locals())

@login_required(login_url='/AS/login/')
def DMS(request):
    name = request.user.username
    return render(request,"DMS/main.html",locals())

@login_required(login_url='/AS/login/')
def DormitoryApply(request):
    #判斷是否為管理員
    name = request.user.username
    ac = Account.objects.get(user=request.user)
    try:
        gender = StudentInfo.objects.get(account=ac).gender
        if gender=='M':
            gd = True
    except:
        gd = True
    start = settings.STARTTIME
    end = settings.ENDTIME
    now = datetime.datetime.now()
    if now>start and now<end:   #開放
        #誰申請 哪個系 年級 學號 姓名 哪一棟宿舍 申請時間 審核狀態
        #宿舍房間狀況 eg. OF 5層樓 20個房間 4個人
        return render(request, "DMS/DormitoryApply.html", locals())
    else:   #不開放
        return render(request, "DMS/main.html", locals())

@login_required(login_url='/AS/login/')
def DormCheck(request):
    name = request.user.username
    account = Account.objects.get(user=request.user)
    try:
        gender = StudentInfo.objects.get(account=account).gender
        if gender=='M':
            gd = True
    except:
        gd = True
    if  account.permission==0:  #管理員
        DormRecords = DormRecord.objects.all()
        dorms = []
        for dormRecord in DormRecords:
            try:
                dorm = DormInfo.objects.get(account=dormRecord.account)
                result = dorm.building+dorm.room+dorm.bed
            except:
                now = datetime.datetime.now()
                end = settings.ENDTIME
                if now>end:
                    result = "銘謝惠顧"
                else:
                    result = "尚未開始分發"
            dm = {
                'D1': DormRecord.Dorms[dormRecord.order1][1],
                'D2': DormRecord.Dorms[dormRecord.order2][1],
                'result': result
            }
            try:
                dm.setdefault('D3',DormRecord.Dorms[dormRecord.order3][1])
            except:
                dm.setdefault('D3','')
            dorms.append(dm)
        return render(request, "DMS/DormCheck.html", locals())
    elif request.method=='POST':    #學生
        name = request.user.username
        D1 = request.POST['Dorm1']
        D2 = request.POST['Dorm2']
        try:
            D3 = request.POST['Dorm3']
        except:
            D3 = 9
        if D1==D2 or D2==D3 or D1==D3:
            error = "志願序不可重複"
            return render(request, "DMS/DormitoryApply.html",locals())
        else:
            try:
                student = StudentInfo.objects.get(account = account)
            except:
                error = "此用戶並非學生"
                return render(request, "DMS/DormitoryApply.html",locals())
            if DormRecord.objects.filter(account=account):
                error = "不可重複申請"
                return render(request, "DMS/DormitoryApply.html",locals())
            with transaction.atomic():
                DormRecord.objects.create(account=account,order1 = D1,order2=D2,order3=D3)
                message = "申請成功"
                return render(request, "DMS/main.html", locals())
    else:
        ac = Account.objects.get(user=request.user)
        try:
            dorm = DormRecord.objects.get(account = ac)
        except:
            error = "查無此資料!!!"
            return render(request,"DMS/main.html",locals())
        D1 = DormRecord.Dorms[dorm.order1][1]
        D2 = DormRecord.Dorms[dorm.order2][1]
        try:
            D3 = DormRecord.Dorms[dorm.order3][1]
        except:
            D3 = ''
        try:
            dorminfo = DormInfo.objects.get(account=ac)
            result = dorminfo.building+dorminfo.room+dorminfo.bed
        except:
            end = settings.ENDTIME
            now = datetime.datetime.now()
            if now < end:
                result = "尚未分發"
            else:
                result = "銘謝惠顧"
        try:
            student = StudentInfo.objects.get(account = ac)
        except:
            error = "此用戶並非學生"
            return render(request, "DMS/main.html", locals())
        dorms = []
        dm = {
            'D1': D1,
            'D2': D2,
            'D3': D3,
            'result': result
        }
        dorms.append(dm)
        return render(request,"DMS/DormCheck.html",locals())

@login_required(login_url='/AS/login/')
def DormDelete(request):
    ac = Account.objects.get(user = request.user)
    try:
        dm = DormRecord.objects.get(account = ac)
        dm.delete()
        message = "刪除成功!!!"
        return render(request,"DMS/main.html",locals())
    except:
        error = "查無此資料!!!"
        return render(request,"DMS/main.html",locals())

@login_required(login_url='/AS/login/')
def DormDistribution(request):
    DormRecords = DormRecord.objects.all().order_by('?')
    #先分發志願序一
    count = 0
    for Record in DormRecords:
        #print(Record)
        Student = StudentInfo.objects.get(account=Record.account)
        try:
            dm = DormInfo.objects.filter(account__isnull=True,building=Record.Dorms[Record.order1][1],gender=Student.gender)
            dm[0].account = Record.account
            dm[0].save()
        except:
            try:
                dm = DormInfo.objects.filter(account__isnull=True, building=Record.Dorms[Record.order2][1],
                                             gender=Student.gender)
                dm[0].account = Record.account
                dm[0].save()
            except:
                try:
                    dm = DormInfo.objects.filter(account__isnull=True, building=Record.Dorms[Record.order3][1],
                                                 gender=Student.gender)
                    dm[0].account = Record.account
                    dm[0].save()
                except:
                    print('QQ')
        print(count)
        count+=1
    return render(request,"DMS/main.html",locals())
"""
def DormInfoCreate(request):
    # OE 280 男 1~5  14rooms/floor
    # OA1 240 男 1~4 15rooms/floor
    # 綜宿 320 男  3~4 40rooms/floor
    # OF 280 女 1~5 14rooms/floor
    # OA2 128 女 5~6 16rooms/floor
    # OB 360 女 1~6 15rooms/floor
    for i in range(1,7):
        for j in range(1,16):
            for k in range(1,5):
                DormInfo.objects.create(building="OB",room=str(i)+str(j).zfill(2),bed=k,status='None',gender='F')
                print(i,j,k)

    return render(request,"DMS/DMS.html",locals())
"""
"""
def DormRecordCreate(request):
    Students = StudentInfo.objects.all()
    i = 0
    for Student in Students:
        ac = Student.account
        try:
            DormRecord.objects.get(account=ac)  ##該學生已經申請過了
        except:
            if Student.gender=='M':
                seq = [0,1,2]
                order = random.sample(seq,k=3)
                DormRecord.objects.create(account=ac,order1=order[0],order2=order[1],order3=order[2])
            else:
                seq = [1,2]
                order = random.sample(seq,k=2)
                DormRecord.objects.create(account=ac,order1=order[0],order2=order[1],order3=9)
        print(i)
        i+=1
    return render(request,"DMS/DMS.html",locals())
"""
