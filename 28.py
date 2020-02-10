import numpy as np
def generateTheSquareMatrix(size):
    if size % 2 == 0:
        raise Exception('size must be an odd number')
    matrix = [ [None for y in range(size)] for x in range(size)]
    # there are total size/2 sub squares in the matrix
    square_count = 1
    x, y = size//2, size//2
    initialNumber = 1
    matrix[x][y] = initialNumber
    while square_count <= size // 2:
        numberGeneratedEachTime = square_count * 2
        x, y = x - 1, y + 1
        # generating a square by 4 directions started from this order: Right, Bottom, Left and Up.
        # Right edge
        count = 0
        while count < numberGeneratedEachTime:
            initialNumber += 1
            x += 1
            count += 1
            matrix[x ][y ] = initialNumber
        # Bottom edge
        count = 0
        while count < numberGeneratedEachTime:
            initialNumber += 1
            y -= 1
            count += 1
            matrix[x ][y ] = initialNumber 
        # Left edge
        count = 0
        while count < numberGeneratedEachTime:
            initialNumber += 1
            x -= 1
            count += 1
            matrix[x ][y ] = initialNumber 
        # Top edge
        count = 0
        while count < numberGeneratedEachTime:
            initialNumber += 1
            y += 1
            count += 1
            matrix[x ][y ] = initialNumber 
        square_count += 1
    return matrix

def sumOfNumbersOnDiagonals(size):
    matrix = generateTheSquareMatrix(size)
    turnLimit = size // 2
    count = 1
    total = 1
    x , y = size//2, size//2
    while count <= turnLimit:
        total += matrix[x + count][y+count] + matrix[x + count][y-count] + matrix[x - count][y+count] + matrix[x - count][y-count]
        count += 1
    print(total)

sumOfNumbersOnDiagonals(1001)
