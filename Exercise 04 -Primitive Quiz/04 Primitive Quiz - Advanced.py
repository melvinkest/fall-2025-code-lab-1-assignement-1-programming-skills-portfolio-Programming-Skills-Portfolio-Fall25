# Storing the correct answer in a variable
italy='Rome'
portugal='Lisbon'
unitedkingdom='London'
russia='Moscow'
switzerland='Bern'
netherlands='Amsterdan'
germany='Berlin'
france='Paris'
sweden='Stockholm'
norway='Oslo'
# Displaying a welcome message
print('Welcome to "Guess the Capital"')
print('Answer the Following!')
print('                              ')

# Beginning of the Quiz

# Dot notation lower was added to the If else statement to convert every response 
# to lowercase and compare to the correct answer which is converted to lowercase.

# This allows the code accept every type of answer in being uppercase or lowercase or mixed.

capital=str(input('What is the Capital of Italy? '))
if capital.lower()==italy.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of Portugal? '))
if capital.lower()==portugal.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of United Kingdom? '))
if capital.lower()==unitedkingdom.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of Russia? '))
if capital.lower()==russia.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of Switzerland? '))
if capital.lower()==switzerland.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of Netherlands? '))
if capital.lower()==netherlands.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of Germany? '))
if capital.lower()==germany.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of France? '))
if capital.lower()==france.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of Sweden? '))
if capital.lower()==sweden.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')

capital=str(input('What is the Capital of Norway? '))
if capital.lower()==norway.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')
print('                 ')
# Displaying a Ending message.
print('Well Done!')