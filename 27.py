from primeNumber import isPrimeNumber
def producePrimeNumberFromQuadraticFormula(a, b, n):
    return n * n + a * n + b
def getNumberOfPrimeFromQuaraticFormula(a, b):
    # start from n = 0
    count = 0
    n = 0
    possiblePrimeNumber = producePrimeNumberFromQuadraticFormula(a, b, n)
    while isPrimeNumber(possiblePrimeNumber):
        count += 1
        n += 1
        possiblePrimeNumber = producePrimeNumberFromQuadraticFormula(a, b, n)
    return count
bestCoefficientA = 0
bestCoefficientB = 0
longestConsecutiveGeneratedPrime = 0
for a in range (-999, 1000):
    for b in range(-1000, 1001):
        numberOfPrime = getNumberOfPrimeFromQuaraticFormula(a, b)
        if longestConsecutiveGeneratedPrime < numberOfPrime:
            bestCoefficientA, bestCoefficientB = a, b
            longestConsecutiveGeneratedPrime = numberOfPrime
print( bestCoefficientB * bestCoefficientA)



