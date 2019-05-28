from django.shortcuts import render

# Create your views here.

def hello(request):
    message = "Hello World!!"
    return render(request,"DMS/hello.html",locals())

def DMS(request):
    return render(request,"DMS/DMS.html",locals())

def DormitoryApply(request):
    return render(request,"DMS/DormitoryApply.html",locals())
