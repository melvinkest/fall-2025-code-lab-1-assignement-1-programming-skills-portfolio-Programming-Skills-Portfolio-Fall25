# Setting the correct password that provides access
password = "12345"
attempts = 0

# Loop runs as long as attempts are under 5
while attempts < 5:
    password_attempt = input("Enter the password: ")

    if password_attempt == password:
        print("Access Granted.")
        break  # This immediately stops the loop
    
    # If code reaches here, the password was wrong
    attempts += 1
    
    # Check if that was their last allowed try
    if attempts == 5:
        print("Maximum attempts reached. Access Blocked.")
    else:
    # Calculate and show how many tries represent the difference    
        print(f"Wrong password. {5 - attempts} attempts remaining.")