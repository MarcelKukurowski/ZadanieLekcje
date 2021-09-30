import datetime as dt
import calendar

print(dt.datetime.now())
print(dt.date.today())
print(dt.timedelta(0,3600))
a = str(dt.datetime.now())
b = str(dt.time(8,00,00))

now = dt.datetime.now()
current_time = now.strftime('%H:%M:%S')
current_date = now.strftime('%w')
time = dt.time(8,00)

print(current_time)
print(current_date)
print(str(time))
