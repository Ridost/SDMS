from django.shortcuts import render,redirect
from AS.models import Account,Repairment,Report
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.generic import View
import datetime

# Create your views here.


@login_required(login_url='/AS/login/')
def index(request):
    user = Account.objects.get(user=request.user)
    messege=user.permission
    return render(request,"RS/index.html",locals())


@login_required(login_url='/AS/login/')
def RepairmentApply(request):

    if request.method == 'POST':
        user = Account.objects.get(user=request.user)
        name = user.user
        locate = request.POST['Locate']
        category = request.POST['Category']
        discribe = request.POST['discribe']
        comment=request.POST['comment']
        state= '已回報'
        if discribe == '' or comment == '':
            messege = '請確認損壞物件描述及方便前往維修時間是否正確填寫'
            render(request,"RS/RepairmentApply.html",locals())
        else:
            with transaction.atomic():
                Repairment.objects.create(
                    publisher=user, location=locate, category=category, content=discribe,
                    state=state, data=datetime.datetime.now(),
                )
    else:
        messege='HEHE'
    return render(request, "RS/RepairmentApply.html", locals())

@login_required(login_url='/AS/login/')
def RepairmentCheck(request):

    return render(request, "/RS/RepairmentCheck.html", locals())


@login_required(login_url='/AS/login/')
def ReportApply(request):

    return render(request, "RS/ReportApply.html", locals())
