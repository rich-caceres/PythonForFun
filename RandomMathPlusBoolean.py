import math

for i in range(1,6):
    print ("number " + str(i))
else:
    i = 3+4
    print("3+4= " + str(i));

    i = math.pi + math.sqrt(2);

    print("3.14 + sqrt(2)= " + str(i));

    i = math.cos(30) + math.sin(30);

    print("cos30 + sin30 expressed in radians is " + str(math.radians(i)));

    print("enter three numbers: (after each number press enter)")
    x = input();
    y = input();
    z = input();
    
    print("{:<6}{:<6}{:<6}".format(x, y, z));

    print("Enter the radius of the circle:")
    r = int(input());
    def findCircArea(r):
        return math.pi * (r*r);
    print("The area of a circle with a radius of " + str(r) + " is: " + str(findCircArea(r)));

    print("Enter two numbers and Python will evaluate and return the largest number: (after each number press enter)")
    x = int(input());
    y = int(input());

    print("The greatest number between " + str(x) + " and " + str(y) + " is: " + str(max(x, y)));

    A = True;
    B = False;

    print("The negation of two boolean variables is: " + str(A and B));

    
    print("Adding the first 10 non integer numbers with a for loop: ");
    l=0
    for i in range(1, 11):
        l = l+i;
        print(str(l));
    else:
            print("Now with a while Loop!\n")

    l=0
    i=1
    while i <= 10:
      l= l+i;
      print(str(l));
      i+=1;
    
