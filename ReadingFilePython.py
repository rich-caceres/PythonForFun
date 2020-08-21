
values=[];

file = open("sometext.txt","rt");

data= file.read();
words= data.split();

file.close()

file = open("sometext.txt","rt")
for lines in file:
    values.append(lines.split());

print('The number of lines in the txt file: ', len(values));
print('The number of words in the txt file: ', len(words))

file.close()
