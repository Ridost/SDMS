from django.shortcuts import render
from django.contrib import auth

from django.http import HttpResponse

from AS.models import StudentInfo, Billboard, BorrowRecord, Account, Package
import datetime

def ShowBillboard(request):
    """
    取出公佈欄的資料，並判斷當前登入者是不是管理員
    """
    billboard = Billboard.objects.all()

    # 是不是管理員
    is_manager = False

    user = Account.objects.get(user = auth.get_user(request))

    if user.permission <= 1:
        is_manager = True

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

def ShowPackage(request):
    is_manager = False

    user = Account.objects.get(user = auth.get_user())

    if user.permission <= 1:
        is_manager = True



    return HttpResponse('package.html', locals())