#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
from primeNumber import isPrimeNumber
import math

number = 600851475143
primeFactor = 0
for x in range ( 2, int(math.sqrt(number)) + 1):
    if(number % x == 0):
       if(isPrimeNumber(x)):
            primeFactor = x
print(primeFactor)            