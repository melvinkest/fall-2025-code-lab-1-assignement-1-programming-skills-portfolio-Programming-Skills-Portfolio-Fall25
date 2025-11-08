password=('12345')
attempt=''
while attempt != password:
    attempt=input('Enter password:')
    if attempt != password:
        print('Incorrect password')

print('Access Granted! You have successfully logged in.')