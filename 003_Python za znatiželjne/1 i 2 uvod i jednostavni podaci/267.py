from datetime import date
import calendar
my_date = date(1566, 9, 7)
md = date(2021, 11, 16)
print()
print(calendar.day_name[my_date.weekday()])
print()
print(md-my_date)
