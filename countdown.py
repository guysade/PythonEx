import datetime
from time import time
def timeTillDate(year,month,day):
    date = datetime.datetime.now()
    x = datetime.datetime(year, month, day)
    timeToDate = x - date
    print(timeToDate)

x = input("Enter goal and date seperated by a colon\n")
goal = x.split(':')[0]
date = x.split(':')[1]
year = date.split('.')[2]
month = date.split('.')[1]
day = date.split('.')[0]

deadline = datetime.datetime.strptime(date, "%d.%m.%Y")
print(deadline)
timeTillDate = deadline - datetime.datetime.now()
timeTillDate = str(timeTillDate.days)
print('your goal is to ' + goal + ", you have " + timeTillDate + ' days to do it!') 