# What is the index of the first term in the Fibonacci sequence to contain 1000 digits? where F1 = 1 and F2 = 1
from number import getHowManyDigitsOfANumber, generateFibonacciNumber

f1 = 1
f2 = 1
f3 = generateFibonacciNumber( f1, f2)
indexOfFiboNumber = 3
boundaryDigits = 1000
while( getHowManyDigitsOfANumber(f3) < boundaryDigits ):
    f1 = f2
    f2 = f3
    f3 = generateFibonacciNumber( f1, f2)
    indexOfFiboNumber += 1
print(indexOfFiboNumber)



