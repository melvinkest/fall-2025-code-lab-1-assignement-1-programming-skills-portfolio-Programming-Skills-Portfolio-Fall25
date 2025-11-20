# Defining a 'List' of strings.
names=['Jake','Zac','Ian','Ron','Sam','Dave']

# Ask the user which name they are looking for.
targetname=input('Select a name to search:')

# The 'in' keyword automatically scans the entire list.
# It returns True if it finds an exact match, and False if it doesn't.
if targetname in names:
    print(f'{targetname} found')
else:
    print(f'{targetname} not found')