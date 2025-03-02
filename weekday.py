# weekday.py
# When run, this program will output whether today is a weekday or not
# There is no user input
# Author: Zoe McNamara Harlowe

# Import datetime module and call it 'date'
from datetime import datetime as date

# I think I overcomplicated this code by creating and appending to the empty list 'weekday'
# I had tried to use an if statement at first but it would always print the first line regardless
# At least this way, I could get the if statement working by checking the length of list 'weekend'
weekend = []

# I researched the datetime.now method on: https://docs.python.org/3/library/datetime.html#datetime.datetime.now
# I also learned that weekday() would give the day of the week as an integer from 0 to 6.
# I learned that 0 = Sunday and 6 = Saturday
day_of_week = date.today().weekday()

if day_of_week == 0 or 6:
    weekend.append(day_of_week)

# Now that I have the day of the week as an int, I need to check whether it is a weekday or weekend
if len(weekend) == 1:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday")


