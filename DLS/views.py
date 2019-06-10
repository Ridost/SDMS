from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from AS.models import StudentInfo, Billboard, Account, Package, Equipment, BorrowRecord
import datetime
import json

# Billboard

def IsManager(request):
    user = Account.objects.get(user = auth.get_user(request))
    return user.permission <= 1

def ShowBillboard(request):
    """
    取出公佈欄的資料，並判斷當前登入者是不是管理員
    """
    billboard = Billboard.objects.all()

    # 是不是管理員
    is_manager = IsManager(request)

    return render(request, 'billboard.html', locals())

def AddBillboard(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '').strip('\n')
    now = datetime.datetime.now()

    print(content)

    # get publisher info
    publisher = auth.get_user(request)
    publisher = Account.objects.get(user = publisher)

    # insert into DB
    Billboard.objects.create(title = title, content = content, date = now, publisher = publisher)
    return HttpResponse()

def DeleteBillboard(request):
    print(request.POST.get('id'))
    Billboard.objects.filter(id = request.POST.get('id')).delete()
    return HttpResponse()

def ModifyBillboard(request):

    modify_id = request.POST.get('id', '')
    new_title = request.POST.get('title', '')
    new_content = request.POST.get('content', '')
    new_publisher = auth.get_user(request)

    print("content = " , new_content)

    new_publisher = Account.objects.get(user = new_publisher)

    billboard = Billboard.objects.get(id = modify_id)

    print(billboard)

    billboard.title = new_title
    billboard.content = new_content
    billboard.publisher = new_publisher
    
    billboard.save()
    
    return HttpResponse()

# Package 

def ShowPackage(request):
    is_manager = False

    user = Account.objects.get(user = auth.get_user(request))

    package = None

    if user.permission <= 1:
        is_manager = True
    else:
        # student = StudentInfo.objects.get(account = user)
        package = Package.objects.filter(receiver = user)

    print(is_manager)
        
    return render(request, 'package.html', locals())

def ManagePackage(request):

    package = Package.objects.all()
    return render(request, 'package/manage.html', locals())

def AddPackage(request):
    pass

def VerifyPackage(request):
    id = request.POST.get('id')
    package = Package.objects.get(id = id)
    package.verify = True
    package.save()

    return HttpResponse()

def ModifyPackage(request, id = None):
    
    if request.method == 'GET':
        p = Package.objects.get(id = id)

        date = str(p.date)
        
        return render(request, 'package/modify.html', { 'package' : p , 'date': date})
    # 送出要更改的資料
    elif request.method == 'POST':

        p = Package.objects.get(id = id)

        p.sender = request.POST.get('sender')
        p.category = request.POST.get('category')

        p.receiver = Account.objects.get(user = User.objects.get(username = request.POST.get('receiver')))
        p.date = request.POST.get('date')

        p.save()
        
        # Redirect到管理頁面
        return HttpResponseRedirect('/DLS/package/manage.html')

def DeletePackage(request):
    id = request.POST.get('id')
    package = Package.objects.filter(id = id).delete()

# Borrow Public Space
    
def SpaceView(request):
    is_manager = IsManager(request)

    if is_manager:
        record = BorrowRecord.objects.filter(confirm = False)
        return render(request, 'borrow/manage.html')

def BorrowSpace(request):
    equip = Equipment.objects.all()
    return render(request, 'borrow.html', locals())

def ConfirmSpace(request):
    pass

def CheckSpace(request):
    
    tag = request.POST.get('tag')
    date = request.POST.get('date')
    start_hour = request.POST.get('start_hour')
    borrow_length = request.POST.get('borrow_length')

    start = datetime.datetime.strptime(date, '%Y-%m-%d')
    start = start.replace(hour = int(start_hour))

    end = start
    end = end.replace(hour = end.hour + int(borrow_length))

    Yes = True
    message = ""
    record = BorrowRecord.objects.filter(tag = tag)

    for rec in record:
        if rec.start_time <= start and rec.end_time <= end:
            Yes = False
            end = rec.end_time
        elif rec.start_time >= start and rec.end_time >= end:
            Yes = False
            start = rec.start_time
        elif rec.start_time <= start and rec.end_time >= end:
            Yes = False
        elif rec.start_time >= start and rec.end_time <= end:
            Yes = False
            start = rec.start_time
            end = rec.end_time

    if Yes:
        message = "這個時段沒有人借用!!!"
    elif start < end:
        message = '{0} 與 {1} 之間已經有人借用'.format(start, end)

    ret = {'flag' : Yes, 'message' : message}

    return JsonResponse(ret)