import datetime

month_birth = int(input('Enter month born (1-12): '))
day_birth = int(input('Enter day born (1-31): '))
year_birth = int(input('Enter year vorn (4-digit): '))

current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day
avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

numsecs_1900_dob = (year_birth - 1900 * avg_numsecs_year)