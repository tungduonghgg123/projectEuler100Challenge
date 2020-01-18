from math import sqrt
def findDevisors(n):
    # of a natural number, n > 0
    divisors = []
    for x in range (1, int(sqrt(n)) + 1 ):
        if n % x == 0:
            if x == n / x:
                divisors.append(x)
            else:
                divisors.append(x)
                divisors.append(n//x)
    return divisors
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

