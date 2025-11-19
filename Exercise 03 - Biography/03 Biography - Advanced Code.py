#Declaring the variables by asking the user to input an answer.
#String function was added to help the code accept both string values and integer values.
name=(str(input("what is your name?")))
hometown=(str(input("What is your hometown?")))
age=str(input("How old are you?"))

biography={
    'Name': name,
    'Hometown': hometown,
    'Age': age
}
#Displaying the users response
for key, value in biography.items():
    print(f"{key}:{value}")