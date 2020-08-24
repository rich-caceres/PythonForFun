import random

#FOR TESTING randomNum = 100

#Assigns the random number
randomNum = random.randrange(-100, 101)
#Gets user name
userName= input('Please enter your name:\n')
playAgain = True

def numberSelectionGame(randomNum, userName):
    guesses= 0;
    userGuess= input('Hello ' + userName + ' a random number between -100 to 100 has been selected. Enter your guess:\n')

    #Keeps track of guesses while loop ends once the user exceeds 7 number of guesses
    while guesses < 7:
        guesses = guesses + 1
        if int(userGuess) == randomNum:
            if(guesses <= 1):
                guessStr = 'guess'
                print('You guessed ' + userGuess + ' correctly in ' + str(guesses) + ' ' + guessStr + '.\nThank you '+ userName +' for playing!' )
            else:
                guessStr = 'guesses'
                print('You guessed ' + userGuess + ' correctly in ' + str(guesses) + ' ' + guessStr + '.\nThank you '+ userName +' for playing!' )
            break;
        else:

            #Hint generation begins here
            #Next 4 lines generate a hint relatin to the types of number it is
            if int(userGuess)> 0 and randomNum < 0:
                print('The random number is a negative number.')
            elif int(userGuess)< 0 and randomNum > 0:
                print('The random number is a positive number.')

            #Next 6 lines generate the hint "close hint" as long as the user is within the range
            for x in range(randomNum-10, randomNum-5):    
                if int(userGuess) == x or int(userGuess) == x:
                    print('Your guess is close to the secret number.')
            for x in range(randomNum-5, randomNum+1):
                if int(userGuess) == x or int(userGuess) == x:
                    print('Your guess is very close to the secret number.')

            #Shows what the user guessed and returns number of guesses the user has left
            userGuess = input('you guessed '+ userGuess + ' which is incorrect.\nYou have ' + str(7 - guesses) + ' left.\n Please guess again:\n')
            if guesses == 7:
                print('The number that was generated is ' + str(randomNum) + '. Thanks for playing ' + userName)
            
    #FOR TESTING print(userGuess)

while playAgain == True:
    answer = input('Would you like to play the Number Guessing Game? y/n')
    if answer == 'n':
        playAgain = False
    else:
        numberSelectionGame(randomNum, userName)

#FOR TESTING print(userName)
