# Solution: From the third row ahead, each internal number will acts as a child node of two father nodes right above it. 
# This senario enables cutting branch when it is not neccessary to travel this child node two times ( each time from different path )

from number import readInput

input = readInput('18_input.txt')
rows = len(input)
# need a way to denote which node was discovered and a dictionary to reserve key-values (x,y)-(total) pairs.
def travel(x,y):
    # this is the naive method.
    if( x > rows - 1):
        return 0
    longestRoute = 0
    for i in range ( 0, 2):
        longestRoute = max(longestRoute, travel(x+1, y+i))
    return input[x][y] + longestRoute
print(travel(0,0))
    
