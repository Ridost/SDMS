# Generated by Django 2.0.5 on 2019-06-01 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AS', '0004_auto_20190530_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowrecord',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='borrowrecord',
            name='user',
        ),
        migrations.RemoveField(
            model_name='dorminfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='dormrecord',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='dormrecord',
            name='check_out_date',
        ),
        migrations.RemoveField(
            model_name='dormrecord',
            name='studentID',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='studentID',
        ),
        migrations.AddField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrowrecord',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AS.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dorminfo',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AS.Account'),
        ),
        migrations.AddField(
            model_name='dormrecord',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AS.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dormrecord',
            name='order1',
            field=models.IntegerField(choices=[(0, '綜合'), (1, '學一'), (2, '學二')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dormrecord',
            name='order2',
            field=models.IntegerField(choices=[(0, '綜合'), (1, '學一'), (2, '學二')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dormrecord',
            name='order3',
            field=models.IntegerField(choices=[(0, '綜合'), (1, '學一'), (2, '學二')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AS.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='billinfo',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.Account'),
        ),
        migrations.AlterField(
            model_name='package',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.Account'),
        ),
        migrations.AlterField(
            model_name='repairment',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.Account'),
        ),
        migrations.AlterField(
            model_name='report',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.Account'),
        ),
    ]
