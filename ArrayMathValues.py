

Data = [0, -1, 2, -3, 4, -5, 6, -7, 8];
value= 0;
#produces the sum of the above array.
for x in Data:
    value = value + x;

print("The sum of the array: " + str(value));

#produces the absolute value of the array.
value= 0;
for x in Data:
    value = abs(value + x);

print("The absolute value of the array: " + str(value));
