# Generated by Django 2.0.5 on 2019-06-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AS', '0003_auto_20190604_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='accused',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repairment',
            name='category',
            field=models.CharField(choices=[('AC', '冷氣'), ('Furnitures', '家具'), ('Bathroom', '浴室'), ('Others', '其他'), ('Internet', '網路')], max_length=16),
        ),
    ]
