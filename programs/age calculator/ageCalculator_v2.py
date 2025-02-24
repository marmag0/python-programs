#!/usr/bin/env python3
import sys

#custom errors
class NotRecognizedAnsError(Exception):
    pass
class UnexpectedError(Exception):
    pass
class NotValidYearError(Exception):
    pass


#game exit script
def programEnd():
    print('\nThanks for using our program! See You next time!')
    sys.exit()


#program info                                                                                        
def programInfo():                                                                                   
    print('\nIn this program, You can check your age in the future,')                                
    print('by providing Your birthdate and a future date.')                                          
    print('REMEMBER! Whenever You want to exit program, enter \'/q\' to force quit.') 


#leap year checker
def leapYearChecker(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 'leap year'
    return 'regular year'


#date validator
def dateValidator(year, month, day):
    if month < 1 or month > 12:
        return 1  #invalid month
    
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if leapYearChecker(year) == 'leap year':
        days_in_month[2] = 29  #adjust for leap year

    if 1 <= day <= days_in_month[month]:
        return 0  #valid date
    return 1  #invalid day


#inptu accepting and converting function
def inputAccepting(qtype, min_year):
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
            if qtype == 'b':
                ans = input('Provide your date of birth in format \'YYYY/MM/DD\' or \'YYYY [month name] DD:\' ')
            elif qtype == 'f':
                ans = input('Provide your future date in format \'YYYY/MM/DD\' or \'YYYY [month name] DD:\' ')
            
            if ans == '/q':
                    programEnd()
            
            year = int(ans[0:4])    #checking patterns
            if ans[4] == '/' and ans[7] == '/' and len(ans) == 10:
                month = int(ans[5:7])
                day = int(ans[8:10])
            elif ans[4] == ' ' and len(ans) >= 11 and len(ans) <= 17:
                ans = ans.split()
                if ans[1].lower() not in months:
                    raise NotRecognizedAnsError
                month = int(months[ans[1].lower()])
                day = int(ans[2])
            else:
                raise NotRecognizedAnsError

            if dateValidator(year, month, day) == 0:
                break
            elif  year < min_year:
                raise NotValidYearError
            else:
                raise NotRecognizedAnsError

        except(NotRecognizedAnsError, ValueError):
            print('\nError! Answer not recognized!')
            print()
            continue
        except(NotValidYearError):
            print('\nError! The future year must be greater or equal to birthday year!')
            print()
        except(EOFError):
            print('\nExiting due to EOF.')
            sys.exit()

    birthdayDate = [year, month, day]
    return birthdayDate


#calculations script
def calculations(year, month, day, futureYear, futureMonth, futureDay):
    if futureMonth > month:
        age = futureYear - year
    elif futureMonth == month:
        if futureDay >= day:
            age = futureYear - year
        else:
            age = futureYear - year - 1
    else:
        age = futureYear - year - 1
    
    return age


#program start script
def programBegin():
    print('\nWelcome to the age calculator program!')

    while True: #start/exit game input
        try:
            start = input('Would You like to start the program? y/n | To get more info enter \'i\' ')
            if start == '/q':
                    programEnd()
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
            sys.exit()
            

#main program script
def programAction ():
    birthdayDate = inputAccepting('b', 0)
    futureDate = inputAccepting('f', birthdayDate[0])
    
    year = birthdayDate[0]
    month = birthdayDate[1]
    day = birthdayDate[2]

    futureYear = futureDate[0]
    futureMonth = futureDate[1]
    futureDay = futureDate[2]

    print()
    print(str(year) + '/' + str(month) + '/' + str(day) + ' -> ' + str(futureYear) + '/' + str(futureMonth) + '/' + str(futureDay))
    print()

    print('You will be', calculations(year, month, day, futureYear, futureMonth, futureDay), 'years old!')


#main code structure
def master():
    programBegin()
    programAction()
    programEnd()

#master call
master()