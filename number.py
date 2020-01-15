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


