from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from AS.models import *
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
import datetime

# Create your views here.


@login_required(login_url='/AS/login/')
def main(request):
    user = Account.objects.get(user=request.user)
    messege=user.permission
    return render(request,"RS/main.html",locals())


@login_required(login_url='/AS/login/')
def RepairmentApply(request):
    user = Account.objects.get(user=request.user)
    if request.method == 'POST':
        locate = request.POST['Locate']
        category = request.POST['Category']
        discribe = request.POST['discribe']+'\r\n'+request.POST['comment']
        comment='方便維修時間'+request.POST['comment']
        state= 'Reported'
        if discribe == '' or comment == '':
            messege = '請確認損壞物件描述及方便前往維修時間是否正確填寫'
            render(request,"RS/RepairmentApply.html",locals())
        else:
            with transaction.atomic():
                Repairment.objects.create(
                    publisher=user, location=locate, category=category, content=discribe,
                    state=state, date=datetime.datetime.now(),
                )
            messege='已成功申請'
    else:
        defcategory=''

    return render(request, "RS/RepairmentApply.html", locals())


@login_required(login_url='/AS/login/')
def RepairmentCheck(request):
    user = Account.objects.get(user=request.user)
    permission = user.permission
    STATES = {
        'Reported': '已回報', 'Pending': '等待中', 'WIP': '修復中', 'Done': '已完成',
    }
    CATEGORIES = {
        'AC': '冷氣', 'Furnitures': '家具', 'Bathroom': '浴室', 'Others': '其他', 'Internet': '網路',
    }
    if permission > 1 :
        rec=[]

        if request.method =='POST':
            state = request.POST['viewapply']
            if state == '1':
                stage = 1
                Records = Repairment.objects.filter(publisher=user ,state ='Reported')
            elif state == '2':
                stage = 2
                Records = Repairment.objects.filter(publisher=user, state='WIP')
            else:
                stage = 3
                Records = Repairment.objects.filter(publisher=user, state='Done')

            if len(Records)>0:
                not_empty = 1
                for record in Records:
                    d={
                        'location': record.location,
                        'state': STATES[record.state],
                        'date': record.date,
                        'category': CATEGORIES[record.category],
                        'content': record.content,
                        'id': record.id                    }
                    rec.append(d)
                messege=''
            else:
                messege='沒有正在處理中的報修申請'
            return render(request, "RS/RepairmentCheck.html", locals())
    else:
        if request.method == 'POST':
            state = request.POST['viewapply']
            if state == '1':
                stage = 1
                Records = Repairment.objects.filter(state='Reported')
            elif state == '2':
                stage = 2
                Records = Repairment.objects.filter(state='WIP')
            else:
                stage = 3
                Records = Repairment.objects.filter(state='Done')
            rec = []

            if len(Records) > 0:
                not_empty = 1
                for record in Records:
                    d = {
                        'location': record.location,
                        'state': STATES[record.state],
                        'date': record.date,
                        'category': CATEGORIES[record.category],
                        'content': record.content,
                        'id': record.id}
                    rec.append(d)
    return render(request, "RS/RepairmentCheck.html", locals())


@login_required(login_url='/AS/login/')
def RepairDelete(request,id):
    try:
        Repairment.objects.get(id=id).delete()
        messege = '刪除成功'
        return redirect('/RS/RepairmentCheck')
    except:
        messege = '資料錯誤'
        return render(request, "RS/Repairment.html", locals())


@login_required(login_url='/AS/login/')
def RepairModify(request, id):

    user = Account.objects.get(user=request.user)
    permission = user.permission

    if permission > 1:
        messege = '付費解鎖喔 \(。▽。)/'
    else:
        Record = Repairment.objects.get(id=id)
        state = Record.state
        if state == 'Reported':
            rec = Repairment.objects.filter(id=id).update(state='WIP')
            return render(request, "RS/RepairmentCheck.html", locals())
        elif state == 'WIP':
            rec = Repairment.objects.filter(id=id).update(state='Done')
            return render(request, "RS/RepairmentCheck.html", locals())
        else:
            messege = '資料錯誤，請再試一次'
            return render(request, "RS/RepairmentCheck.html", locals())


@login_required(login_url='/AS/login/')
def ReportApply(request):
    user = Account.objects.get(user=request.user)
    if request.method == 'POST':
        accused = request.POST['accused']
        category = request.POST['Category']
        comment = request.POST['discribe']
        state = 'Reported'
        if comment == '':
            messege = '請確認檢舉描述是否正確填寫'
            render(request, "RS/ReportApply.html", locals())
        else:
            with transaction.atomic():
                Report.objects.create(
                    publisher=user, accused=accused, category=category, content=comment,
                    state=state, date=datetime.datetime.now(),
                )
            messege = '申請成功'
    else:
        messege = ''

    return render(request, "RS/ReportApply.html", locals())


@login_required(login_url='/AS/login/')
def ReportCheck(request):
    user = Account.objects.get(user=request.user)
    permission = user.permission

    CATEGORIES = {
        'Noise': '噪音', 'Dirty': '髒亂', 'Intrusion': '闖入', 'Others': '其他'
    }
    STATES = {
        'Reported': '已回報', 'Pending': '等待中', 'WIP': '處理中', 'Done': '已完成'
    }
    if permission > 1:
        rec=[]

        if request.method =='POST':
            state = request.POST['viewapply']
            if state == '1':
                stage = 1
                Records = Report.objects.filter(publisher=user, state='Reported')
            elif state == '2':
                stage = 2
                Records = Report.objects.filter(publisher=user, state='WIP')
            else:
                stage = 3
                Records = Report.objects.filter(publisher=user, state='Done')

            if len(Records)>0:
                not_empty = 1
                for record in Records:
                    d={
                        'accused': record.accused,
                        'state': STATES[record.state],
                        'date': record.date,
                        'category': CATEGORIES[record.category],
                        'content': record.content,
                        'id': record.id
                    }
                    rec.append(d)
                messege=''
            else:
                messege='沒有正在處理中的報修申請'
            return render(request, "RS/ReportCheck.html", locals())
    else:
        if request.method == 'POST':
            state = request.POST['viewapply']
            if state == '1':
                stage = 1
                Records = Report.objects.filter(state='Reported')
            elif state == '2':
                stage = 2
                Records = Report.objects.filter(state='WIP')
            else:
                stage = 3
                Records = Report.objects.filter(state='Done')
            rec = []

            if len(Records) > 0:
                not_empty = 1
                for record in Records:
                    d = {
                        'accused': record.accused,
                        'state': STATES[record.state],
                        'date': record.date,
                        'category': CATEGORIES[record.category],
                        'content': record.content,
                        'id': record.id}
                    rec.append(d)
    return render(request, "RS/ReportCheck.html", locals())


@login_required(login_url='/AS/login/')
def ReportModify(request, id):

    user = Account.objects.get(user=request.user)
    permission = user.permission

    if permission > 1:
        messege = '付費解鎖喔 \(。▽。)/'
    else:
        Record = Report.objects.get(id=id)
        state = Record.state
        if state == 'Reported':
            rec = Report.objects.filter(id=id).update(state='WIP')
            return render(request, "RS/ReportCheck.html", locals())
        elif state == 'WIP':
            rec = Report.objects.filter(id=id).update(state='Done')
            return render(request, "RS/ReportCheck.html", locals())
        else:
            messege = '資料錯誤，請再試一次'
            return render(request, "RS/ReportCheck.html", locals())


@login_required(login_url='/AS/login/')
def ReportDelete(request, id):
    try:
        Report.objects.get(id=id).delete()
        messege = '刪除成功'
        return redirect('/RS/ReportCheck')
    except:
        messege = '資料錯誤'
        return render(request, "RS/ReportApply.html", locals())
