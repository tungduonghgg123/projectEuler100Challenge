#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math
number = 600851475143
primeFactor = 0
def isPrimeNumber(num):
    for x in range (2, int(math.sqrt(num)) + 1):
        if(num % x == 0):
            return False
    return True
for x in range ( 2, int(math.sqrt(number)) + 1):
    if(number % x == 0):
       if(isPrimeNumber(x)):
            primeFactor = x
print(primeFactor)            