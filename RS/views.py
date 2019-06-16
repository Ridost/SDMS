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
    permission=user.permission
    return render(request, "RS/main.html", locals())


@login_required(login_url='/AS/login/')
def RepairmentApply(request):
    user = Account.objects.get(user=request.user)
    permission = user.permission

    if request.method == 'POST':
        locate = request.POST['Locate']
        category = request.POST['Category']
        discribe = request.POST['discribe']
        state = 'Reported'
        if discribe == '':
            messege = '請確認損壞物件描述是否正確填寫。'
            render(request, "RS/RepairmentApply.html", locals())
        else:
            with transaction.atomic():
                Repairment.objects.create(
                    publisher=user, location=locate, category=category, content=discribe,
                    state=state, date=datetime.datetime.now(),
                )
            messege = '申請成功。'
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
    if permission > 1:
        rec = []
        if request.method == 'POST':
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
                messege='沒有此類別的報修申請紀錄。'
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
            else:
                messege = '沒有此類別的報修申請紀錄。'
    return render(request, "RS/RepairmentCheck.html", locals())


@login_required(login_url='/AS/login/')
def RepairDelete(request, id):
    try:
        Repairment.objects.get(id=id).delete()
        messege = '刪除成功。'
        return render(request, "RS/RepairmentCheck.html", locals())
    except:
        messege = '資料錯誤，請再試一次。如果重複出現此錯誤，請聯絡系統管理員。'
        return render(request, "RS/RepairmentCheck.html", locals())


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
            messege = '資料錯誤，請再試一次。'
            return render(request, "RS/RepairmentCheck.html", locals())


@login_required(login_url='/AS/login/')
def ReportApply(request):
    user = Account.objects.get(user=request.user)
    permission = user.permission

    if request.method == 'POST':
        accused = request.POST['accused']
        category = request.POST['Category']
        comment = request.POST['discribe']
        state = 'Reported'
        if comment == '':
            messege = '請確認檢舉描述是否正確填寫。'
            render(request, "RS/ReportApply.html", locals())
        else:
            with transaction.atomic():
                Report.objects.create(
                    publisher=user, accused=accused, category=category, content=comment,
                    state=state, date=datetime.datetime.now(),
                )
            messege = '申請成功。'
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
            else:
                messege = '沒有此類別的檢舉紀錄。'
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
            else:
                messege = '沒有正在處理中的檢舉項目。'
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
            messege='送出成功。'
            rec = Report.objects.filter(id=id).update(state='WIP')
            return render(request, "RS/ReportCheck.html", locals())
        elif state == 'WIP':
            messege='送出成功。'
            rec = Report.objects.filter(id=id).update(state='Done')
            return render(request, "RS/ReportCheck.html", locals())
        else:
            messege = '資料錯誤，請再試一次。如果重複出現此錯誤，請聯絡系統管理員。'
            return render(request, "RS/ReportCheck.html", locals())


@login_required(login_url='/AS/login/')
def ReportDelete(request, id):
    try:
        Report.objects.get(id=id).delete()
        messege = '刪除成功。'
        return redirect('/RS/ReportCheck')
    except:
        messege = '資料錯誤，請再試一次。如果重複出現此錯誤，請聯絡系統管理員。'
        return render(request, "RS/ReportApply.html", locals())


@login_required(login_url='/AS/login/')
def Conductjudge(request):
    user = Account.objects.get(user=request.user)
    permission = user.permission
    if permission <= 1:
        if request.method == 'POST':
            student = request.POST['accused']
            reason = request.POST['reason']
            point = request.POST['point']
            try:
                user = User.objects.get(username=student)
                account = Account.objects.get(user=user)
                if account.permission == 2:
                    now_conduct = StudentInfo.objects.get(account=account).conduct
                    with transaction.atomic():
                        Conduct.objects.create(
                            student=account, reason=reason, point=point, date=datetime.datetime.now(),
                        )
                        now_conduct = int(now_conduct) + int(point)
                        StudentInfo.objects.filter(account=account).update(conduct=now_conduct)
                    reply = 0
                    messege = '新增成功。'
                    # return render(request, "RS/Conductjudge.html", locals())
                    return redirect('/RS/ConductCheck')
                else:
                    reply = 1
                    messege = '此用戶並非住宿生。'
                    return render(request, "RS/Conductjudge.html", locals())
            except:
                reply = 1
                messege = '查無此資料或輸入錯誤。'
                return render(request, "RS/Conductjudge.html", locals())
        else:
            reply = 1
            messege=''
            return render(request, "RS/Conductjudge.html", locals())
    else:
        try:
            conduct = Conduct.objects.filter(student=user)
            total_point = StudentInfo.objects.get(account=user).conduct
            rec = []
            if len(conduct) > 0:
                for c in conduct:
                    cd = {
                        'id': c.id,
                        'reason': c.reason,
                        'point': c.point,
                        'date': c.date,
                    }
                    rec.append(cd)
                return render(request, 'RS/Conductjudge.html', locals())
        except:
            messege='資料錯誤，請再試一次。如果重複出現此錯誤，請聯絡系統管理員。'
            return render(request, 'RS/Conductjudge.html', locals())


@login_required(login_url='/AS/login/')
def ConductCheck(request):
    user = Account.objects.get(user=request.user)
    permission = user.permission
    if permission <= 1:
        try:
            Record = StudentInfo.objects.filter(conduct__gte=6)
            rec = []
            not_empty = 1
            for c in Record:
                cd = {
                    'account': c.account,
                    'grade': c.grade,
                    'conduct': c.conduct,
                }
                rec.append(cd)
            if len(Record) == 0:
                empty = 1
            return render(request, 'RS/ConductCheck.html', locals())
        except:
            messege = ''
            return render(request, 'RS/ConductCheck.html', locals())
    else:
        return redirect('/RS/main')


@login_required(login_url='/AS/login/')
def conductconfirm(request, id):
    user = Account.objects.get(user=request.user)
    permission = user.permission
    '''
    Record = StudentInfo.objects.get(account=)
    if state == 'Reported':
        messege = '送出成功'
        rec = Report.objects.filter(id=id).update(state='WIP')
        return render(request, "RS/ReportCheck.html", locals())
    elif state == 'WIP':
        messege = '送出成功'
        rec = Report.objects.filter(id=id).update(state='Done')
        return render(request, "RS/ReportCheck.html", locals())
    else:
        messege = '資料錯誤，請再試一次'
        '''
    return render(request, "RS/ReportCheck.html", locals())

