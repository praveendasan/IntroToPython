# date function in python
from datetime import datetime, timedelta

current_dateTime = datetime.now()
# print(str(current_dateTime))
# print(str(current_dateTime.day))
# print(str(current_dateTime.month))
# print(str(current_dateTime.year))
# one_day = timedelta(days=1)
# yesterday = current_dateTime - one_day
# print('yesterday was ' + str(yesterday))

one_day = timedelta(weeks=1)
yesterday = current_dateTime - one_day
print('yesterday was ' + str(yesterday))

birthday = input('Enter your birthday (dd/mm/yyyy)')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: '+ str(birthday_date))
