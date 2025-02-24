#!/usr/bin/env python3
import sys

#custom error
class NotRecognizedAnsError(Exception):
    pass


#game exit script
def programEnd():
    print('\nThanks for using our program! See You next time!')
    sys.exit()


#program info
def programInfo():
    print('\nIn this program, You can check your age in the future,')
    print('by providing Your birthdate and a future date.')
    print('REMEMBER! Whenever You want to exit program, enter \'/q\'')


#program start script
def programBegin():
    print('\nWelcome to the age calculator program!')

    while True: #start/exit game input
        try:
            start = input('Would You like to start the program? y/n | To get more info enter \'i\' ')

            if start == 'y':
                print()
                break
            elif start == 'n' or start == '/q':
                programEnd()
            elif start == 'i':
                programInfo()
                print()
                continue
            else:
                raise NotRecognizedAnsError
        except(NotRecognizedAnsError):
            print('\nError! Answer not recongized!')
            print()
            continue
        except(EOFError):
            print('\nExiting due to EOF.')
            

#main program script
def programAction ():
    months = {'jan': 1, 'january': 1,   #months mapping dict
              'feb': 2, 'february': 2,
              'mar': 3, 'march': 3,
              'apr': 4, 'april': 4, 
              'may': 5,
              'jun': 6, 'june': 6,
              'jul': 7, 'july': 7,
              'aug': 8, 'august': 8,
              'sep': 9, 'september': 9,
              'oct': 10, 'october': 10,
              'nov': 11, 'november': 11,
              'dec': 12, 'december': 12}

    while True: #accepting and validating birthday input
        try:
            ans = str(input('Provide your date of birth in format YYYY/MM/DD or YYYY [moth name] DD: ')).lower()

            

        except(NotRecognizedAnsError):
            print('\nError! Answer not recongized!')
            print()
            continue
        except(EOFError):
            print('\nExiting due to EOF.')



#mmain code structure
def master():
    programBegin()
    programAction()


#master call
master()