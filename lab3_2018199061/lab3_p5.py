import datetime

# person 1

# get month, day, year of birth of person 1
month_birth = int(input('Person 1: Enter month born (1-12): '))
day_birth = int(input('Person 1: Enter day born (1-31): '))
year_birth = int(input('Person 1: Enter year born (4-digit): '))

# get current month, day, year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

# calculate number of seconds in a day, an average month, an average year
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day
avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

# calculate age in seconds
numsecs_1900_dob = ((year_birth - 1900) * avg_numsecs_year) + ((month_birth - 1) * avg_numsecs_month) + (day_birth * numsecs_day)
numsecs_1900_today = ((current_year - 1900) * avg_numsecs_year) + ((current_month - 1) * avg_numsecs_month) + (current_day * numsecs_day)

# save it to variable 'age_in_secs_1'
age_in_secs_1 = numsecs_1900_today - numsecs_1900_dob

# person 2
# re-assigned variables to use them again for person 2

# get month, day, year of birth of person 2
month_birth = int(input('Person 2: Enter month born (1-12): '))
day_birth = int(input('Person 2: Enter day born (1-31): '))
year_birth = int(input('Person 2: Enter year born (4-digit): '))

# calculate number of seconds in a day, an average month, an average year
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day
avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

# calculate age in seconds
numsecs_1900_dob = ((year_birth - 1900) * avg_numsecs_year) + ((month_birth - 1) * avg_numsecs_month) + (day_birth * numsecs_day)
numsecs_1900_today = ((current_year - 1900) * avg_numsecs_year) + ((current_month - 1) * avg_numsecs_month) + (current_day * numsecs_day)

# save it to variable 'age_in_secs_2'
age_in_secs_2 = numsecs_1900_today - numsecs_1900_dob

# calculate and print the distance of age in seconds between player 1 and 2
print(f'Age difference in seconds: {abs(age_in_secs_1-age_in_secs_2)}')