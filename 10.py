# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
from primeNumber import isPrimeNumber
sum = 0
for x in range ( 2, 2 * pow( 10, 6 ) ):
    if( isPrimeNumber( x ) ):
        sum = sum + x
print( sum )
    