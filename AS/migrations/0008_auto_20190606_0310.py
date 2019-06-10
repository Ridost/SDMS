# Generated by Django 2.0.5 on 2019-06-05 19:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AS', '0007_auto_20190606_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowrecord',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='borrowrecord',
            name='start_date',
        ),
        migrations.AddField(
            model_name='borrowrecord',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrowrecord',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dorminfo',
            name='status',
            field=models.CharField(choices=[('Lived', '有住人'), ('None', '沒有住人'), ('Forbid', '不能住')], default='None', max_length=16),
        ),
    ]
