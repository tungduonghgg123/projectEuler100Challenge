import math
import inflect

def findDivisors(n):
    # of a natural number, n > 0
    smallDivisors = []
    bigDivisors = []
    for x in range (1, int(math.sqrt(n)) + 1 ):
        if n % x == 0:
            if x == n / x:
                smallDivisors.append(x)
            else:
                smallDivisors.append(x)
                bigDivisors.append(n//x)
    bigDivisors.reverse()
    return smallDivisors + bigDivisors
def sumOfProperDivisors(number):
    # numbers less than n which divide evenly into n
    sum = 0
    divisors = findDivisors(number)
    for divisor in divisors:
        sum += divisor
    return sum - number

def convertArrayStr2Int(arr):
    return [int(i) for i in arr]
    # second approach
    # return list( map( int, arr ) )
def productOfDigits ( num ):
    string = str ( num )
    product = 1
    for x in range ( 0, len ( string ) ):
        product = product * int ( string[x] )
    return product
def sumOfDigits ( num ):
    string = str ( num )
    sum = 0
    for x in range ( 0, len ( string ) ):
        sum = sum + int ( string[x] )
    return sum

def number2word(num):
    p = inflect.engine()
    return p.number_to_words(num)
def readInput(path):
    # read a 2 dimensional array from 11_input and return a corresponding array.
    f = open(path, 'r')
    output = []
    for x in f:
        output.append(convertArrayStr2Int(x.split()))
    return output
def sumOfDigitsOfAFactorial(number):
    factorial = math.factorial(number)
    return sumOfDigits(factorial)

def getHowManyDigitsOfANumber(number):
    return len(str(number))
def generateFibonacciNumber(f1, f2):
    return f1 + f2
