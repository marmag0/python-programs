#!/usr/bin/env python3

#custom errors
class OutsideRangeError(Exception):
    pass

#checks and converts the month to an appropriate integer
def monthChecker(month):
    jan = ['jan', 'january', 'Jan', 'January']
    feb = ['feb', 'february', 'Feb', 'February']
    mar = ['mar', 'march', 'Mar', 'March']
    apr = ['apr', 'april', 'Apr', 'April']
    may = ['may', 'May']
    jun = ['jun', 'june', 'Jun', 'June']
    jul = ['jul', 'july', 'Jul', 'July']
    aug = ['aug', 'august', 'Aug', 'August']
    sep = ['sep', 'september', 'Sep', 'September']
    oct = ['oct', 'october', 'Oct', 'October']
    nov = ['nov', 'november', 'Nov', 'November']
    dec = ['dec', 'december', 'Dec', 'December']

    if month in jan:
        month = 1
    elif month in feb:
         month = 2
    elif month in mar:
        month = 3
    elif month in apr:
        month = 4
    elif month in may:
        month = 5
    elif month in jun:
        month = 6
    elif month in jul:
        month = 7
    elif month in aug:
        month = 8
    elif month in sep:
        month = 9
    elif month in oct:
        month = 10
    elif month in nov:
        month = 11
    elif month in dec:
        month = 12

    return month

#checks if leap year
def lepYearChecker(year):
    if year % 100 == 0 and year % 400 == 0:
        return 'leap year'
    elif year % 4 == 0 and year % 100 != 0:
        return 'leap year'
    elif year % 4 == 0 and year % 100 == 0:
        return 'regular year'
    else:
        return 'regular year'
    
#main code
print('Welcome to the age calculator!')

#program start
while True:
    ans = input('Would you like to know how old you will be in particular year? Answear y/n ')

    if ans == 'n':
        print('Thanks for using our program. Exiting...')
        exit()
    elif ans == 'y':
        break
    else:
        print('Wrong answear! Try again!')
        continue

#accepting input year value
while True:
    try:
        year = int(input('What year were you born? '))
        break
    except ValueError:
        print('Error! The year input must be an integer!')
        continue

#checking the year type
yearType = lepYearChecker(year)

#accepting input month value
while True:
    try:
        month = input('In what month were you born? ')

        if month.isdigit() is True:
            month = int(month)
        else:
            month = int(monthChecker(month))
        
        if month >= 1 and month <= 12:
            break
        else:
            raise OutsideRangeError
    except (ValueError, OutsideRangeError):
        print('Error! The month input must be an integer or valid month name!')
        continue

#accepting input day value
while True:
    try:
        day  = int(input('On what day? '))

        if month == 2 and yearType == 'regular year': 
            maxDay = 28
        elif month == 2 and yearType == 'leap year':
            maxDay = 29
        elif month % 2 == 0 and month != 2:
            maxDay = 31
        elif month % 2 != 2:
            maxDay = 30
        
        if day >= 1 and day <= maxDay:
            break
        else:
            raise OutsideRangeError
    except (ValueError, OutsideRangeError):
        print('Error! The year input must be an valid integer!')
        continue

#accepting input futureYear value
while True:
    try:
        futureYear = int(input('What year did you want to know about? '))
        break
    except ValueError:
        print('Error! The year input must be an integer!')
        continue

#checking the futureYear type
futureYearType = lepYearChecker(futureYear)

#accepting input futureMonth value
while True:
    try:
        futureMonth = input('What month did you want to know about? ')

        if futureMonth.isdigit() is True:
            futureMonth = int(futureMonth)
        else:
            futureMonth = int(monthChecker(futureMonth))
        
        if futureMonth >= 1 and futureMonth <= 12:
            break
        else:
            raise OutsideRangeError
    except (ValueError, OutsideRangeError):
        print('Error! The month input must be an integer or valid month name!')
        continue

#accepting input futureDay value
while True:
    try:
        futureDay  = int(input('What day did you want to know about? '))

        if futureMonth == 2 and futureMonth == 'regular year': 
            maxDay = 28
        elif futureMonth == 2 and futureMonth == 'leap year':
            maxDay = 29
        elif futureMonth % 2 == 0 and futureMonth != 2:
            maxDay = 31
        elif futureMonth % 2 != 2:
            maxDay = 30
        
        if futureDay >= 1 and futureDay <= maxDay:
            break
        else:
            raise OutsideRangeError
    except (ValueError, OutsideRangeError):
        print('Error! The year input must be an valid integer!')
        continue

#confirmation output
print('OK, so you were born on:', str(year) + '-' + str(month) + '-' + str(day))
print('...and You would like to know about:', str(futureYear) + '-' + str(futureMonth) + '-' + str(futureDay))

#calculations
if month < futureMonth:
    age = futureYear - year
elif month == futureMonth:
    if day <= futureDay:
        age = futureYear - year
    elif day > futureDay:
        age = futureYear - year - 1
elif month > futureMonth:
    age = futureYear - year - 1

#exiting
timestampNow = str(year) + '-' + str(month) + '-' + str(day)
timestampFuture = str(futureYear) + '-' + str(futureMonth) + '-' + str(futureDay)
print(timestampNow, '->', timestampFuture)
print('I the year', futureYear, 'you will be', age, 'years old!')
print()
print('Thanks for using our program. Exiting...')
exit()