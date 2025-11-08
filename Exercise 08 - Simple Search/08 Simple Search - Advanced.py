names=['Jake','Zac','Ian','Ron','Sam','Dave']

targetname=str(input('Select a name to search:'))
if targetname in names:
    print(f'{targetname} found')
else:
    print(f'{targetname} not found')