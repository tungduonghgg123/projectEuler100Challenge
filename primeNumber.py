import math
def isPrimeNumber(num):
    # handle special cases
    for x in range (2, int(math.sqrt(num)) + 1):
        if(num % x == 0):
            return False
    return True
