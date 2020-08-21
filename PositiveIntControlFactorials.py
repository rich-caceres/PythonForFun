

while True:
    inputNumber = input("Enter a positive integer: ");
    try:
        num = int(inputNumber)
        if num<0:
            print("Not a positive integer!")
        else:
            break;
    except ValueError:
           print("This is not a number!")

factorial = 1    
for i in range (1, num + 1):
    factorial = factorial * i;
print("factorial of ", inputNumber, " is: ", factorial)



