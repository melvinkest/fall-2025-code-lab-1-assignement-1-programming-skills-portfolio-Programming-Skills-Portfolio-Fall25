#Declaring the Variables
france='Paris'
#Asking for user input 
capital=str(input('What is the Capital of France? '))
if capital.lower()==france.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')