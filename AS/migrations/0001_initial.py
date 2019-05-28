# Generated by Django 2.2.1 on 2019-05-28 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('tag', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('current_state', models.CharField(choices=[('Free', '可借用'), ('InUse', '出借中'), ('NotAvailable', '不可使用')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('studentID', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=1)),
                ('department', models.CharField(max_length=16)),
                ('grade', models.CharField(choices=[('1', '一年級'), ('2', '二年級'), ('3', '三年級'), ('4', '四年級')], max_length=1)),
                ('room', models.CharField(max_length=8)),
                ('bed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('Noise', '噪音'), ('Dirty', '髒亂'), ('Intrusion', '闖入'), ('Others', '其他')], max_length=16)),
                ('content', models.CharField(max_length=512)),
                ('state', models.CharField(choices=[('Reported', '已回報'), ('Pending', '等待中'), ('WIP', '處理中'), ('Done', '已完成')], max_length=16)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.StudentInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Repairment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('AC', '冷氣'), ('Furnitures', '家具'), ('Bathroom', '浴室'), ('Others', '其他')], max_length=16)),
                ('content', models.CharField(max_length=512)),
                ('state', models.CharField(choices=[('Reported', '已回報'), ('Pending', '等待中'), ('WIP', '修復中'), ('Done', '已完成')], max_length=16)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.StudentInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('Mail', '信件'), ('Package', '包裹'), ('Prompt', '限時')], max_length=2)),
                ('sender', models.CharField(max_length=32)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.StudentInfo')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('phone_number', models.CharField(max_length=16)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('memo', models.CharField(max_length=512)),
                ('state', models.CharField(choices=[('Free', '可借用'), ('InUse', '出借中'), ('NotAvailable', '不可使用')], max_length=16)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='BillInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('content', models.CharField(max_length=512)),
                ('state', models.CharField(choices=[('Unpaid', '未繳費'), ('Paid', '已繳費'), ('Expired', '過期')], max_length=2)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.StudentInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=512)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.StudentInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='0000', max_length=32)),
                ('Permission', models.IntegerField(choices=[(0, '系統管理員'), (1, '宿舍管理員'), (2, '住宿生'), (3, '學生')])),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AS.StudentInfo')),
            ],
        ),
    ]
