from arrow import now

now_time = now()

year = now_time.year
month = now_time.month
day = now_time.day
print("year:", year)
print("month:", month)
print("day:", day)