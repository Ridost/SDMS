import subprocess

subsystems = ['AS', 'BMS', 'DLS', 'DMS', 'RS']
model_list = ['Account,StudentInfo', 'Account,StudentInfo,Package', \
    'StudentInfo,Billboard,Account,Package,Equipment,BorrowRecord', \
    'Account,StudentInfo,DormRecord,DormInfo,BillInfo,System', \
    'Account,StudentInfo,Repairment,Report,Equipment' ]

# generate views class
for i in range(5):
    src = subsystems[i]+'//views.py'
    des = subsystems[i]+'_views'
    subprocess.run(['pyreverse', '-ASmy', src, '-p', des])
subprocess.run(['move', '*.dot', 'src//', '/y'])

# return to root dir of django project
subprocess.run(['cd', '..//..//'])

# generate db_schema
for i in range(5):
    des = 'docs//diagrams//src//'+subsystems+'_db_schema.dot'
    subprocess.run(['python', 'manage.py', 'graph_models', '-a', '-I',\
        model_list[i], '>', des])
