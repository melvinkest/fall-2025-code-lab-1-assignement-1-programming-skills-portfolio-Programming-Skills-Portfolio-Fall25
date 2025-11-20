#Setting the list
days_data= {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
month= int(input('Enter a month number (1-12):'))
if month in days_data:
    # We only need to ask about leap years if the month is 2.
    # Asking the user if the year is a leap year
    if month == 2: 
            # .strip() removes spaces, .lower() converts to lowercase.
            # This ensures "  YES ", "Yes", and "yes" are all treated the same.
            leap = input("Is the year a leap year? (yes/no): ").strip().lower()
            
            # Checking the user's response
            if leap == 'yes':
                days_data[2] = 29  # Adjusting February's days to 29
            elif leap != 'no': 
                # Handling input that isn't clearly 'yes' or 'no'(e.g., "maybe")
                print("Invalid response for leap year status. Assuming non-leap year (28 days).")
    
    # Retrieve the value using the key
    result_days = days_data[month]
    print(f"Month {month} has {days_data} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")