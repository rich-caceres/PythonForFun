
inpName = input('Enter your name')
inpPassword = input('Enter a password')


while True:
    name = input('Enter name to sign in')
    password = input('Enter password to sign in')
    if name != inpName and password != inpPassword:
        print('Access Denied')
    else:
        break
    

print('Access Granted')
