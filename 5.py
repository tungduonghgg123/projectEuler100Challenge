import math
def lcm ( a, b ):
    return int(a * b / math.gcd( a, b))
def lcmInRange ( start, end):
    sharedLCM = start
    for x in range ( start + 1, end ):
        sharedLCM = lcm( sharedLCM, x)
    return sharedLCM
print(lcmInRange( 2, 20 ))
