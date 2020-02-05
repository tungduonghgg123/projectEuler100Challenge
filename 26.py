# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# WORTH TO NOTICE:
# from this site : https://math.stackexchange.com/questions/287805/the-longest-repeating-decimal-that-can-be-created-from-a-simple-fraction
# I know that the repeating decimal period can't exceed the denominator. 
# So the longest possible period of repeating decimal has to be 9,98 or less.

from decimal import getcontext, Decimal
import re
# If a decimal possesses repeating period, then its period has to show up in this interval.
precision = 998 * 2

def getDecimalPart(numerator, denominator, precision = precision):
    getcontext().prec = precision
    fraction = Decimal(numerator) / Decimal(denominator)
    if fraction % 1 == 0:
        raise Exception('The fraction is not a decimal')
    fractionInStringFormat = str(fraction)
    behindTheDot = fractionInStringFormat.split('.')[1]
    return behindTheDot

def getAllIndexOfACharacter(character, string):
    return [m.start() for m in re.finditer(character, string)]
def detectPeriod(decimal):
    for i in range(len(decimal)):
        indexOfStart = 0
        startOfPeriod = decimal[indexOfStart]
        period = ''
        possibleIndexOfAdjacentPeriod = getAllIndexOfACharacter(startOfPeriod, decimal)
        del possibleIndexOfAdjacentPeriod[0]
        if len(possibleIndexOfAdjacentPeriod) == 0:
            # remove this non repeating digit
            decimal = decimal[1:]
            continue
        for index in possibleIndexOfAdjacentPeriod:
            period = decimal[indexOfStart: index]
            lengthOfPeriod = len(period)
            adjacentPeriod = decimal[index: index + lengthOfPeriod ]
            if adjacentPeriod == period:
                if verifyPeriod(decimal, period):
                    return period
        # remove this non repeating digit
        decimal = decimal[1:]
    return '0'
        
def verifyPeriod(decimal, period):
    lengthOfPeriod = len(period)
    possibleNumberOfPeriods = len(decimal) // lengthOfPeriod
    sufficeTestTime = 10
    if possibleNumberOfPeriods > sufficeTestTime:
        possibleNumberOfPeriods = sufficeTestTime
    count = 0
    while(count < possibleNumberOfPeriods):
        start = lengthOfPeriod * count
        end = start + lengthOfPeriod
        if not decimal[start : end] == period:
            return False
        count += 1
    return True

def getRecurringPeriod(numerator, denominator):
    decimal = getDecimalPart(numerator, denominator)
    return detectPeriod(decimal)
def getLongestRecurringPeriod():
    longestPeriod = 0
    denominator = 1
    for x in range(2, 1000):
        length = len(getRecurringPeriod(1, x))
        if longestPeriod < length:
            longestPeriod = length
            denominator = x
    print(denominator)
getLongestRecurringPeriod()

     



