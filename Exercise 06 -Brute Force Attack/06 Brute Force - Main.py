# Setting the correct password that provides access
password=('12345')

# Initialize the variable with an empty string so the while loop can start
attempt=''

# Keep looping as long as the user's attempt does NOT match the password
while attempt != password:
    attempt=input('Enter password:')

# Checking if the input is wrong to provide correct feedback    
    if attempt != password:
        print('Incorrect password')

# This line only runs after the loop breaks (meaning the password was correct)
print('Access Granted! You have successfully logged in.')