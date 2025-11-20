def check_even_odd(number):
    #This function determines if a value is even or odd
    #and returns a message.
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

def main():
    # Ask the user for a number within the main function
    try:
        user_input = int(input("Please enter a number: "))
        
        # Pass the number to the function
        # The function returns a message
        message = check_even_odd(user_input)
        
        # Print the returned message from within the main function
        print(message)
        
    except ValueError:
        print("Invalid input. Please enter a whole number (integer).")

# Standard boilerplate to call the main function
if __name__ == "__main__":
    main()