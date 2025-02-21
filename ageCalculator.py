#!/usr/bin/env python3

print('Welcome to the age calculator!')

while True:
    ans = input('Would you like to know how old you will be in particular year? Answear y/n ')
    if ans == 'n':
        print('Thanks for using our programm. Exiting...')
        exit()
    elif ans == 'y':
        break
    else:
        print('Wrong answear! Try again!')
        continue

year = int(input('What year were you born? '))
future = int(input('What year did you want to know about? '))

age = future - year

print('I the year', future, 'you will be', age, 'years old!')
print('Thanks for using our programm. Exiting...')
exit()