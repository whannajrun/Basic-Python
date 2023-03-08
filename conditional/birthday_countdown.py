'''
[DISCLAIMER] This is a customized case from spring club explorer held by generation girl 

Case: 
Create a program displaying number of days
left before user's next birthday (countdown).

Rules:
- Full name input process must be done once
- Calculate age from birthday year (no input)
- Use if/else 
- Expected Output: last_name, countdown, next_age

'''

#Display:
  # Hello, Ms. [last_name]
  # It's [countdown] days left before your [next_age] birthday


#Answer
from datetime import datetime

full_name = input("Input your full name: ")

birthday_year = int(input("Input your birthday year [YYYY]: "))
birthday_month = int(input("Input your birthday month: "))
birthday_day = int(input("Input your birthday day: "))

name_split = full_name.split(" ")
last_name = name_split[-1]

dt_now = datetime.now()

dt = datetime(dt_now.year,birthday_month, birthday_day)

age = dt_now.year-birthday_year

if (dt.month, dt.day) <= (dt_now.month, dt_now.day):
  age += 1
  days_left = (datetime(dt_now.year+1, dt_now.month, dt_now.day) - dt).days+1
else:
  days_left = (dt-dt_now).days+1


print("Hello, Ms.", last_name, 
     "\nIt's", days_left, "days left before your",age,"birthday")