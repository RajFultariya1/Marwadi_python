'''import datetime
x=datetime.datetime.now()
print(x)'''

import datetime
x=datetime.datetime.now()
print(x.year)
print("day of the week:",x.strftime("%A"))
print("day of the week:",x.strftime("%a"))
print("Date",x.strftime("%d"))
print("month",x.strftime("%m"))
print("month",x.strftime("%B"))
print("month",x.strftime("%b"))
print("year",x.strftime("%b"))
print("year",x.strftime("%Y"))
print('time:',x.strftime('%H:%M:%S'))
print('ddmyyyy',x.strftime('%d-%m-%y'))
