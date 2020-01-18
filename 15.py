# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Solution1: Considering the starting point in the 20-20 grid as (0, 0) and the destination as (20,20).
# The total route can be made for a (x,y) point will be denoted as r(x,y)
# As a result, r(x,y) = r(x+1,y) + r(x,y+1) if x,y < 20. Otherwise, r(x,y) = 1
# I will calculate the result recursively .

n = 20 


def findPathRecursively(x, y):
    # Oops, stack over flow for n is more than 12 => find another way!
    if x == n or y == n:
        return 1
    return findPathRecursively(x+1, y) + findPathRecursively(x, y+1)

# Solution 2: calculate from tail to head. Say no to recursion.
# TODO: change loop in range to something readable
def findPathByLoop():
    # generate a 2d array, in which the elements in the right and bottom edge are 1.
    def generateArray():
        size = n + 1
        return [[None] * (size-1) + [1]] * (size-1) + [[1]*size]

    a = generateArray()
    for x in range(n-1, -1, -1):
        for y in range(n-1, -1, -1):
            a[x][y] = a[x+1][y]+ a[x][y+1] 
    print(a[0][0])

findPathByLoop()
