from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    PERMISSIONS = (
        (0, '系統管理員'),
        (1, '宿舍管理員'),
        (2, '住宿生'),
        (3, '學生')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Permission = models.IntegerField(choices=PERMISSIONS)


class Billboard(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=128)
    publisher = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    content = models.CharField(max_length=512)


class Repairment(models.Model):
    CATEGORIES = (
        ('AC', '冷氣'),
        ('Furnitures', '家具'),
        ('Bathroom', '浴室'),
        ('Others', '其他')
    )

    STATES = (
        ('Reported', '已回報'),
        ('Pending', '等待中'),
        ('WIP', '修復中'),
        ('Done', '已完成')
    )

    date = models.DateField()
    publisher = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    category = models.CharField(max_length=16, choices=CATEGORIES)
    content = models.CharField(max_length=512)
    state = models.CharField(max_length=16, choices=STATES)


class Report(models.Model):
    CATEGORIES = (
        ('Noise', '噪音'),
        ('Dirty', '髒亂'),
        ('Intrusion', '闖入'),
        ('Others', '其他')
    )

    STATES = (
        ('Reported', '已回報'),
        ('Pending', '等待中'),
        ('WIP', '處理中'),
        ('Done', '已完成')
    )

    date = models.DateField()
    publisher = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    category = models.CharField(max_length=16, choices=CATEGORIES)
    content = models.CharField(max_length=512)
    state = models.CharField(max_length=16, choices=STATES)


class StudentInfo(models.Model):
    GENDERS = (
        ('M', '男'),
        ('F', '女')
    )

    GRADES = (
        ('1', '一年級'),
        ('2', '二年級'),
        ('3', '三年級'),
        ('4', '四年級')
    )

    studentID = models.ForeignKey('Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=1, choices=GENDERS)
    department = models.CharField(max_length=16)
    grade = models.CharField(max_length=1, choices=GRADES)
    room = models.CharField(max_length=8)
    bed = models.IntegerField()


class BillInfo(models.Model):
    STATES = (
        ('Unpaid', '未繳費'),
        ('Paid', '已繳費'),
        ('Expired', '過期')
    )

    account = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    content = models.CharField(max_length=512)
    state = models.CharField(max_length=2, choices=STATES)


class Equipment(models.Model):
    STATES = (
        ('Free', '可借用'),
        ('InUse', '出借中'),
        ('NotAvailable', '不可使用')
    )

    tag = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=32)
    current_state = models.CharField(max_length=16, choices=STATES)


class BorrowRecord(models.Model):
    STATES = (
        ('Free', '可借用'),
        ('InUse', '出借中'),
        ('NotAvailable', '不可使用')
    )

    tag = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    user = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=16)
    start_date = models.DateField()
    end_date = models.DateField()
    memo = models.CharField(max_length=512)
    state = models.CharField(max_length=16, choices=STATES)


class Package(models.Model):
    CATEGORIES = (
        ('Mail', '信件'),
        ('Package', '包裹'),
        ('Prompt', '限時')
    )

    date = models.DateField()
    category = models.CharField(max_length=2, choices=CATEGORIES)
    receiver = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    sender = models.CharField(max_length=32)


