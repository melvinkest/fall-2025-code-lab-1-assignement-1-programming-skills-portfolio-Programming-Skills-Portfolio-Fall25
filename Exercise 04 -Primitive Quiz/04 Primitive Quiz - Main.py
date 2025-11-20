# Storing the correct answer in a variable
france='Paris'
# Ask the user for their guess. 
capital=input('What is the Capital of France? ')

# Convert BOTH the user's guess and the correct answer to lowercase.
# This ensures that 'paris', 'PARIS', and 'Paris' all match.
if capital.lower()==france.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')