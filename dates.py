### Dates ###
from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

now = datetime.now()
print(now)

timestamp = now.timestamp()
print(timestamp)


def print_date(date):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)


print_date(now)

timestamp = now.timestamp()
print(timestamp)

year_2023 = datetime(2023, 1, 1)
print(year_2023)

current_time = time(21, 6, 10)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today()
print(current_date)
print(current_date.year)

current_date = date(2023, 3, 20)
print(current_date)
print(current_date.day)

current_date = date(current_date.year + 1,
                    current_date.month + 1, current_date.day + 1)
print(current_date)

diff = now.date() - year_2023.date()
print(diff)

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta / start_timedelta)
