import random

#FOR TESTING randomNum = 100
randomNum = random.randrange(-100, 101)
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
            if int(userGuess)> 0 and randomNum < 0:
                print('The random number is a negative number.')
            elif int(userGuess)< 0 and randomNum > 0:
                print('The random number is a positive number.')
                
            for x in range(randomNum-10, randomNum-5):    
                if int(userGuess) == x or int(userGuess) == x:
                    print('Your guess is close to the secret number.')
            for x in range(randomNum-5, randomNum+1):
                if int(userGuess) == x or int(userGuess) == x:
                    print('Your guess is very close to the secret number.')

            
                
            userGuess = input('you guessed '+ userGuess + ' which is incorrect.\nYou have ' + str(7 - guesses) + ' left.\n Please guess again:\n')
            if guesses == 7:
                print('The number that was generated is ' + str(randomNum) + '. Thanks for playing ' + userName)
            
    #FOR TESTING print(userGuess)

numberSelectionGame(randomNum, userName)

#FOR TESTING print(userName)
