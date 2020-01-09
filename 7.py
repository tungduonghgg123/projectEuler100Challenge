#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

from primeNumber import isPrimeNumber

count = 0
i = 2
while ( count < 10001 ):
    if ( isPrimeNumber( i )):
        count = count + 1
    i = i + 1
print( i - 1 )