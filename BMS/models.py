from django.db import models

# Create your models here.
class FileModel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/%Y%m%d/')
