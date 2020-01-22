# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
from day import M, T, W, R, F, S, U, determineDay, isLeapYear

def countSundays():
    year = 1901
    # 1 Jan 1901 is Tuesday
    firstDayOfAMonth = T
    sundayCounter = 0

    while year < 2001:
        month = 1
        while(month < 13):
            if month == 9 or month == 4 or month == 6 or month == 11 :
                firstDayOfAMonth = determineDay(firstDayOfAMonth, 30)
            elif month == 2:
                if isLeapYear(year):
                    firstDayOfAMonth = determineDay(firstDayOfAMonth, 29)
                else:
                    firstDayOfAMonth = determineDay(firstDayOfAMonth, 28)
            else:
                firstDayOfAMonth = determineDay(firstDayOfAMonth, 31)

            if firstDayOfAMonth == S:
                sundayCounter += 1
                
            month += 1
        year +=1
    return sundayCounter

print(countSundays())