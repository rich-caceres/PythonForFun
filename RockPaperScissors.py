import random

choice= ['r','p','s']
win = 0
loss = 0
draw = 0


answer=input('Would you like to play rock, paper, scissors? y/n')

def newPlayer():
    name = input('Enter your name to play!')
    return name

def computerChoice(choice):
    i = random.randrange(0,3)
    return choice[i]    

def playerChoice():
    playerChoice = input('Please choose between (r)ock, (p)aper, (s)cissors')
    return playerChoice()

if answer == 'y':
    name = newPlayer()
else:
    exit(0)

computerChoice(choice)
