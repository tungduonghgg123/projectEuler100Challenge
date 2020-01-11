# We deprive this equation from the given problem: 2000a + 200b = 1000^2 + 2ab <=> a = ( 1000^2 - 2000b )/( 2000 - 2b )
# With condition: a + b is less than 1000 and they are natural numbers. 
# I will create a loop from 0 to less than 1000, each index I will consider as a value for b, if the deprived a is a natural number then I will calculate c. 
# if c is eligible then the problem is solved.
a = 0
for b in range ( 0, 1000 ):
    a =(pow( 1000, 2 ) - 2000 * b )/( 2000 - 2 * b )
    if( a.is_integer() and a >= 0):
        a = int( a )
        c = 1000 - a - b
        if c > b and b > a:
            print(a)
            print(b)
            print(c)
            print( a * b * c)
        