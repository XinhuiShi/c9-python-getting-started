# print today's date
from datetime import datetime, timedelta
today = datetime.now()
print(today)
# print yesterday's date
one_day = timedelta(days = 1)
yesterday = today - one_day
print(yesterday)
# ask a user to enter a date
randomDay = input('Enter a day (DD/MM/YYYY): ')
# print the date one week from the date entered
forRD = datetime.strptime(randomDay, '%d/%m/%Y')
print(forRD)