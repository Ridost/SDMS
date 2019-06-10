from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


class PackageAdmin(admin.ModelAdmin):
    list_display = ['category', 'sender', 'receiver', 'date']
    search_fields = ['category', 'sender', 'receiver', 'date']
    ordering = ['date']

    def __str__(self):
        return str(self.pk)


class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['account', 'gender', 'department', 'grade']
    search_fields = [ 'gender', 'department', 'grade']
    ordering = ['account']

    def __str__(self):
        return str(self.account.user)

class DormInfoAdmin(admin.ModelAdmin):
    list_display = ['account', 'building', 'room', 'bed']
    search_fields = ['account', 'building', 'room', 'bed']
    ordering = ['account']

    def __str__(self):
        return str(self.account.user)

class DormRecordAdmin(admin.ModelAdmin):
    list_display = ['account','order1','order2','order3']
    search_fields = ['account','order1','order2','order3']
    ordering = ['account']

    def __str__(self):
        return str(self.account.user)

class BillAdmin(admin.ModelAdmin):
    list_display = ['account','content','state','year']
    search_fields =['content','state','year']
    ordering = ['content']

# Register your models here.
admin.site.register(Account)

# DMS
admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.register(DormInfo,DormInfoAdmin)
admin.site.register(DormRecord,DormRecordAdmin)

# DLS
admin.site.register(Billboard)
admin.site.register(Equipment)
admin.site.register(Package, PackageAdmin)
admin.site.register(BorrowRecord)
