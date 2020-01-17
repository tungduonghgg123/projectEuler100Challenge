# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner. 
# How many such routes are there through a 20×20 grid?

# Solution: Considering the starting point in the 20-20 grid as (0, 0) and the destination as (20,20).
# The total route can be made for a (x,y) point will be denoted as r(x,y)
# As a result, r(x,y) = r(x+1,y) + r(x,y+1) if x,y < 20. Otherwise, r(x,y) = 1
# I will calculate the result recursively .

n = 15

def findPath(x,y):
    if x == n or y == n:
        return 1
    return findPath(x+1,y) + findPath(x,y+1)

print(findPath(0,0))

