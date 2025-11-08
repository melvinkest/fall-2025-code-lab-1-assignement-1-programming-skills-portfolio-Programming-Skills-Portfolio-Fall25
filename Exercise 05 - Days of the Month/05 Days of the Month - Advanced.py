days= {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
month= int(input('Enter a month number (1-12):'))
if month in days:
    if month == 2: 
            # Ask the user if the year is a leap year
            leap = input("Is the year a leap year? (yes/no): ").strip().lower()
            
            # Check the user's response
            if leap == 'yes':
                days[2] = 29  # Adjust February's days to 29
            elif leap != 'no':
                 # Handle input that isn't clearly 'yes' or 'no'
                print("Invalid response for leap year status. Assuming non-leap year (28 days).")
    days = days[month]
    print(f"Month {month} has {days} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")