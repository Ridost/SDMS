from django.contrib import admin
from django.contrib.auth.models import User
from .models import Account

# Register your models here.
admin.site.register(Account)