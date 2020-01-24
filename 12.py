# What is the value of the first triangle number to have over five hundred divisors?
from number import findDivisors

def triangleNumberGenerator(i):
    return i*(i+1)/2
found = False
i = 0
while(not found):
    triNum = triangleNumberGenerator(i)
    if len(findDivisors(triNum)) > 500:
        found = True
        print(triNum)
    i = i + 1

