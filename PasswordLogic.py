
inpName = input('Enter your name \n')
inpPassword = input('Enter a password \n')


while True:
    name = input('Enter name to sign in \n')
    password = input('Enter password to sign in \n')
    
    if name != inpName:
        print('no such username')
    if password != inpPassword:
        print('Access Denied') 
    if name == inpName and password == inpPassword:
        break

print('Access Granted')
