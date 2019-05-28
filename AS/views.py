from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from .models import *

# Create your views here.
def current_datetime(request):
	now = datetime.datetime.now()
	html = '<html><body>It is now %s.</body></html>' % now
	return HttpResponse(html)

def convert_permission(perID):
	'''
	PERMISSIONS = (
        (0, '系統管理員'),
        (1, '宿舍管理員'),
        (2, '住宿生'),
        (3, '學生')
    )
	'''
	convert_table = ['系統管理員', '宿舍管理員', '住宿生', '學生']
	return convert_table[perID]

@login_required(login_url='/AS/login/')
def index(request):
	stuID = request.user.username
	name = request.user.first_name
	user = Account.objects.get(user=request.user)
	permission = convert_permission(user.permission)
	message='Login successed!'
	return render(request, 'AS/index.html', locals())

def login(request):
	message = 'Wellcome please login!'
	if request.user.is_authenticated:
		return redirect('/AS/index/')
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/AS/index/')		
			else:
				message = 'Account is not active, please login again!'
				return render(request, 'AS/login.html', locals())
		else:
			message = 'Login failed!'
	return render(request, 'AS/login.html', locals())

@login_required(login_url='/AS/login/')
def logout(request):
	auth.logout(request)
	return redirect('/AS/login/')
	message = 'Logout successed!'
'''
@login_required(login_url='/AS/login/')
def sign(request):
	if request.method == 'POST':
		name=request.POST['username']
		firstname = request.POST['firstname']
		password = request.POST['password']
		password2 = request.POST['password2']
		if password!=password2:
			message='Please input same password!'
			return render(request,"AS/sign.html",locals())
		try:
			User.objects.get(username=name)
			message="帳號已有人使用"
			return render(request, "AS/sign.html", locals())			
		except:
			pass
		user=User.objects.create_user(name, mail, password,first_name=firstname)
		user.is_active=True		#信箱認證會用到 還沒做
		user.save()
		detail=user_detail.objects.create(user=user,phone=user_phone)
		return redirect('/account/login/')
	return render(request, "account/sign.html", locals())
'''