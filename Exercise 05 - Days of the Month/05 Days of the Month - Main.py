# Create a Dictionary (Lookup Table). 
# Left side = Key (Month Number), Right side = Value (Days in that month)
days= {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

# Convert the input immediately to an integer so we can look it up
month= int(input('Enter a month number (1-12):'))

# Checking if the user's input exists as a 'Key' in our dictionary
if month in days:
# Retrieve the 'Value' associated with that Key    
    result = days[month]
    print(f"Month {month} has {days} days.")
else:
    # Handle cases where the user types 13, 0, or -5
    print("Invalid month number. Please enter a number between 1 and 12.")