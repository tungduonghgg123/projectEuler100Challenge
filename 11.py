# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?


from number import convertArrayStr2Int


def readInput():
    # read a 2 dimensional array from 11_input and return a corresponding array.
    f = open('11_input.txt', 'r')
    output = []
    for x in f:
        output.append(convertArrayStr2Int(x.split()))
    return output


def findGreatestProductHorizontally(arr, interval=4):
    length = len(arr)
    daddyProduct = 0
    for x in range(0, length):
        for y in range(0, length - interval + 1):
            product = arr[x][y] * arr[x][y + 1] * arr[x][y + 2] * arr[x][y + 3]
            if product > daddyProduct:
                daddyProduct = product
    return daddyProduct


def findGreatestProductVertically(arr, interval=4):
    length = len(arr)
    daddyProduct = 0
    for x in range(0, length):
        for y in range(0, length - interval + 1):
            product = arr[y][x] * arr[y+1][x] * arr[y+2][x] * arr[y+3][x]
            if product > daddyProduct:
                daddyProduct = product
    return daddyProduct


def findGreatestProductDiagonally(arr, interval=4):
    length = len(arr)
    daddyProduct = 0
    # Major diagonal
    for x in range(0, length - interval + 1):
        for y in range(0, length - interval + 1):
            product = arr[x][y] * arr[x+1][y+1] * arr[x+2][y+2] * arr[x+3][y+3]
            if product > daddyProduct:
                daddyProduct = product

    # Minor diagonal
    for x in range(0, length - interval + 1):
        for y in range(3, length):
            product = arr[x][y] * arr[x+1][y-1] * arr[x+2][y-2] * arr[x+3][y-3]
            if product > daddyProduct:
                daddyProduct = product
    return daddyProduct


input = readInput()
print(findGreatestProductDiagonally(input))
print(findGreatestProductVertically(input))
print(findGreatestProductHorizontally(input))
