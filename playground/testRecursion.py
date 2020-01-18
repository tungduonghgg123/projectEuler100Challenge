def GreatestCommonDivisor(x,y):
    #  still works because the depth is short
    if y == 0:
        return x
    return GreatestCommonDivisor(y, x%y) 
# print(GreatestCommonDivisor(500000000000000000000000000,10000000000000000000000000))
n = 400
def sumRecursively(x):
# n is how many time
    if x == n:
        return 1
    # live
    return 1 + sumRecursively(x+1) 
    # die
    # return 1 + sumRecursively(x+1) + sumRecursively(x+2) 
# => the depth is so fucking long this time
print( sumRecursively(0))