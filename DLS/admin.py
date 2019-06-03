from django.contrib import admin
<<<<<<< HEAD
from AS.models import Billboard
# Register your models here.

admin.site.register(Billboard)
=======
from AS.models import Billboard, StudentInfo, Equipment, BorrowRecord
# Register your models here.

admin.site.register(Billboard)
admin.site.register(StudentInfo)
admin.site.register(Equipment)
admin.site.register(BorrowRecord)
>>>>>>> DLS
