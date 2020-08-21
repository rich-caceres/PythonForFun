import random

#FOR TESTING
randomNum = -100
#randomNum = random.randrange(-100, 101)
userName= input('Please enter your name:\n')

def numberSelectionGame(randomNum, userName):
    guesses= 0;
    userGuess= input('Hello ' + userName + ' a random number between -100 to 100 has been selected. Enter your guess:\n')

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
            if int(userGuess) == randomNum-10 and randomNum > 0:
                print('Your guess is close and the secret number is positive.')
            elif int(userGuess) == randomNum+10 and randomNum < 0:
                print('Your guess is close and the secret number is negative.')
            userGuess = input('you guessed '+ userGuess + ' which is incorrect.\nYou have ' + str(7 - guesses) + ' left.\n Please guess again:\n')
            if guesses == 0:
                print('The number that was generated is ' + str(randomNum) + ' thanks for playing ' + userName)
            
    #FOR TESTING print(userGuess)

numberSelectionGame(randomNum, userName)
#FOR TESTING print(userName)
