import calendar
inp=list(map(int,input().split()))
dd=inp[1]
mm=inp[0]
yy=inp[2]
day=calendar.weekday(yy,mm,dd)
dayName=calendar.day_name[day]
print(dayName.upper())