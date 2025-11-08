days= {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
month= int(input('Enter a month number (1-12):'))
if month in days:
    days = days[month]
    print(f"Month {month} has {days} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")