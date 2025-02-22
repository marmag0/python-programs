#!/usr/bin/env python3

#custom errors
class NotRecognisedAns (Exception):
    pass


#display rules
def displayRules():
    print()
    print('Simple word guessing game between 2 players,') 
    print('where one player chooses the word and the second player tries to guess it.')

    print('The guessing player puts in a letter or the whole word for each guess (like a hangman).')
    print('If the letter is in the word, the word will be printed with all the correct letters in the appropriate spot.') 
    print('If the player guesses a letter that is not in the word, the player loses one guessing attempt.')

    print('If the player guesses all the letters before they run out of guessing attempts, they win.') 
    print('If not, they lose :((')
    print()

#exiting
def gameExit():
    print('Exiting the game... Thanks for playing...')
    exit()


#initialization
def gameInit():
    print()
    print('Welcome to the word guessing game!')

    while True:
        try:
            option = input('write \'START\' to begin | write \'RULES\' to display rules | write \':q\' to exit ')

            if option == 'START':
                print()
                break
            elif option == 'RULES':
                displayRules()
                continue
            elif option == ':q':
                exit()
            else:
                raise NotRecognisedAns        
        except (NotRecognisedAns):
            print('Error! Answear not regonised!')
            print()
            continue


#game start
def gameStart():
    print('PLAYER 1 turn:')
    word = input('Please enter a word for your opponent: ')

    chanses = 7
    guessed = False
    corectLetters = []
    guessedLetters = []
    wrongLetters = []
    wordInProgress = []

    blank = ''
    for letter in word:
        blank = blank + '_'
        corectLetters.append(letter)
        wordInProgress.append('_')


    while guessed is False and chanses > 0:
        print()
        print('PLAYER 2 turn:')
        print('Wrong letters:', wrongLetters, ' | ', 'Tries left:', chanses)

        try: 
            guess = input('Guess the letters or the word: ' + str(blank) + ' ')
            print()

            if not guess.isalpha():
                raise NotRecognisedAns
        except (NotRecognisedAns):
            print('Error! Insert a proper value!')
            continue

        if guess in guessedLetters:
            print('You\'ve already guessed that...')
        elif guess in corectLetters and guess not in guessedLetters:
            counter = 0
            for letter in word:
                if guess == letter:
                    wordInProgress[counter] = str(letter)
                    counter += 1
                else:
                    counter += 1
                    continue
            guessedLetters.append(guess)
            blank = ''.join(wordInProgress)
        elif guess == word:
            print('Congrtulations, you guessed the word \'' + str(word) + '\'')
            guessed = True
        else:
            chanses -= 1
            if len(guess) == 1:
                print('There is no such letter in this word!')
                wrongLetters.append(guess)
            else:
                print('This word is incorrect!')

    if guessed == True:
        return 0
    elif guessed == False:
        return 1
    else:
        print('Unexpected Error!')
        exit()


#game end
def gameEnd (result):
    print()
    if result == 0:
        print('Congrts! You Won!')
    elif result == 1:
        print('You loose! Maybe next time...')
    

    print('Thnaks for playing! See you next time :D')


#master function
def master():
    gameInit()
    result = gameStart()
    gameEnd(result)


#startup function recall
master()