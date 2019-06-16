from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required

from AS.models import StudentInfo, Billboard, Account, Package, Equipment, BorrowRecord
import datetime
import json

# Billboard

@login_required(login_url='/AS/login/')
def IsManager(request):
    user = Account.objects.get(user = auth.get_user(request))
    return user.permission <= 1

@login_required(login_url='/AS/login/')
def ShowBillboard(request):
    """
    取出公佈欄的資料，並判斷當前登入者是不是管理員
    """
    billboard = Billboard.objects.all()

    # 是不是管理員
    is_manager = IsManager(request)

    return render(request, 'main.html', locals())


def ShowSpecificBillboard(request, id = None):
    if id == None:
        return HttpResponseRedirect("../")
    
    is_manager = IsManager(request)
    billboard = Billboard.objects.get(id = int(id))

    if not billboard:
        return HttpResponseRedirect("../")

    return render(request, 'billboard/showbillboard.html', locals())

def AddBillboard(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '').strip('\n')
    now = datetime.datetime.now()

    # get publisher info
    publisher = auth.get_user(request)
    publisher = Account.objects.get(user = publisher)

    # insert into DB
    Billboard.objects.create(title = title, content = content, date = now, publisher = publisher)
    return HttpResponse()

def DeleteBillboard(request):
    Billboard.objects.get(id = int(request.POST.get('id'))).delete()
    return HttpResponse()

def ModifyBillboard(request):

    modify_id = request.POST.get('id', '')
    new_title = request.POST.get('title', '')
    new_content = request.POST.get('content', '')
    new_publisher = auth.get_user(request)

    new_publisher = Account.objects.get(user = new_publisher)

    billboard = Billboard.objects.get(id = modify_id)

    billboard.title = new_title
    billboard.content = new_content
    billboard.publisher = new_publisher
    billboard.date = datetime.datetime.now()
    
    billboard.save()
    
    return HttpResponse()



# Package 

@login_required(login_url='/AS/login/')
def ShowPackage(request):


    is_manager = IsManager(request)
    package = None

    if not is_manager:
        package = Package.objects.filter(receiver = Account.objects.get(user = auth.get_user(request)))
        
    return render(request, 'package.html', locals())

def ManagePackage(request):
    is_manager = IsManager(request)
    package = Package.objects.filter(verify=False)

    return render(request, 'package/manage.html', locals())

def AddPackage(request):
    pass

def VerifyPackage(request):
    id = request.POST.get('id')
    package = Package.objects.get(id = id)
    package.verify = True
    package.save()

    return HttpResponse()

# Borrow Public Space

# for manager


@login_required(login_url='/AS/login/')
def ShowRecord(request):
    is_manager = IsManager(request)
    record = BorrowRecord.objects.all().order_by('-confirm')

    return render(request, 'borrow/showall.html', locals())


@login_required(login_url='/AS/login/')
def ManageRecord(request):
    is_manager = IsManager(request)
    record = BorrowRecord.objects.filter(confirm = 0)
    
    return render(request, 'borrow/manage.html', locals())

def ConfirmRecord(request):
    id = request.POST.get('id')

    record = BorrowRecord.objects.get(id = id)
    record.confirm = 1
    record.save()

    return HttpResponse()
    
def WithdrawRecord(request):
    id = request.POST.get('id')

    record = BorrowRecord.objects.get(id = id)
    record.confirm = 2
    record.save()

    return HttpResponse()
    
# for student

@login_required(login_url='/AS/login/')
def BorrowSpace(request):

    if request.method == 'POST':

        ret = CheckSpace(request)
        data = json.loads(ret.content)

        print(data)

        if data['flag'] == False:
            return HttpResponseRedirect("../status/")

        equip = request.POST['tag']
        space = Equipment.objects.get(tag=equip)

        date = request.POST['date']
        start_hour = request.POST['start_hour']
        borrow_length = request.POST['borrow_length']
        memo= request.POST['memo']
        applicant = Account.objects.get(user=auth.get_user(request))

        start_time = datetime.datetime.strptime(date, '%Y-%m-%d')
        start_time = start_time.replace(hour = int(start_hour))

        end_time = start_time.replace(hour=start_time.hour + int(borrow_length))

        BorrowRecord.objects.create(tag=space, account=applicant, start_time=start_time, end_time=end_time, memo=memo, confirm=0)
        return HttpResponseRedirect("../status")

        

    is_manager = IsManager(request)
    equip = Equipment.objects.all()

    return render(request, 'borrow/apply.html', locals())

@login_required(login_url='/AS/login/')
def CheckSpace(request):
    
    tag = request.POST.get('tag')
    date = request.POST.get('date')
    start_hour = request.POST.get('start_hour')
    borrow_length = request.POST.get('borrow_length')
    try: 
        start = datetime.datetime.strptime(date, '%Y-%m-%d')
        start = start.replace(hour = int(start_hour))
    except ValueError:
        return HttpResponse()

    end = start
    end = end.replace(hour = end.hour + int(borrow_length))

    Yes = True
    message = "這個時段沒有人借用!!!"
    record = BorrowRecord.objects.filter(tag = tag)


    for rec in record:
        if start >= rec.start_time and start < rec.end_time:
            Yes = False
            end = rec.end_time
        elif end >= rec.start_time and end < rec.end_time:
            Yes = False
            start = rec.start_time
        elif end < rec.end_time and start > rec.start_time:
            Yes = False
        elif end >= rec.end_time and start <= rec.end_time:
            Yes = False
            start = rec.start_time
            end = rec.end_time

    if not Yes and start < end:
        message = '{0} 與 {1} 之間已經有人借用'.format(start, end)

    print(start, end)

    ret = {'flag' : Yes, 'message' : message}

    return JsonResponse(ret)

@login_required(login_url='/AS/login/')
def ShowStatus(request):
    is_manager = IsManager(request)
    record = BorrowRecord.objects.filter(account = Account.objects.get(user = auth.get_user(request)))
    
    return render(request, 'borrow/showstatus.html', locals())