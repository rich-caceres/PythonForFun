import random

choice= ['Rock','Paper','Scissors']
win = 0
loss = 0
draw = 0


answer=input('Would you like to play rock, paper, scissors? y/n')

def newPlayer():
    name = input('Enter your name to play!\n')
    return name

def randomChoice(choice):
    i = random.randrange(0,3)
    return choice[i]    

def playerChoice():
    playerChoice = input('Please choose between (r)ock, (p)aper, (s)cissors or (q) to quit\n')
    return playerChoice

if answer == 'y':
    name = newPlayer()
else:
    exit(0)


while True:
    computerChoice = randomChoice(choice)
    answer = playerChoice()

        
    # draw logic
    if computerChoice == 'Rock' and answer == 'r':
        draw = draw + 1
        print('The computer chose ', computerChoice, ', its a draw.\n')
    elif computerChoice == 'Scissors' and answer == 's':
        draw = draw + 1
        print('The computer chose ', computerChoice, ', its a draw.\n') 
    elif computerChoice == 'Paper' and answer == 'p':
        draw = draw + 1
        print('The computer chose ', computerChoice, ', its a draw.\n')

    #loss logic
    if computerChoice == 'Rock' and answer == 's':
        loss = loss + 1
        print('The computer chose ', computerChoice, ', you lost.\n')
    elif computerChoice == 'Scissors' and answer == 'p':
        loss = loss + 1
        print('The computer chose ', computerChoice, ', you lost.\n')
    elif computerChoice == 'Paper' and answer == 'r':
        loss = loss + 1
        print('The computer chose ', computerChoice, ', you lost.\n')

    #win logic
    if computerChoice == 'Rock' and answer == 'p':
        win = win+ 1
        print('The computer chose ', computerChoice, ', you win!\n')
    elif computerChoice == 'Scissors' and answer == 'r':
        win = win + 1
        print('The computer chose ', computerChoice, ', you win!\n')
    elif computerChoice == 'Paper' and answer == 's':
        win = win + 1
        print('The computer chose ', computerChoice, ', you win!\n')

    if answer == 'q':
        break

    print('This is your current score\nWins:', win,'\nLosses:', loss, '\nDraws: ', draw)
