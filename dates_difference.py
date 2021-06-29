'''
03/03/2001
13/08/2001
163 days
'''


import datetime

date1 = list(map(int, input().split("/")))
date2 = list(map(int, input().split("/")))

sdate = datetime.date(date1[2],date1[1],date1[0])
edate = datetime.date(date2[2],date2[1],date2[0])


print(str(edate - sdate)[:-9])
