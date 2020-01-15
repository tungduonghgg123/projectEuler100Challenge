# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

from number import convertArrayStr2Int


def readInput():
    # read a 2 dimensional array from 11_input and return a corresponding array.
    f = open('13_input.txt', 'r')
    output = []
    for x in f:
        output.append(x.split()[0])
    return convertArrayStr2Int(output)


numArr = readInput()
sum = 0
for num in numArr:
    sum = sum + num

length = len(str(sum))
print(sum//pow(10, length - 10))
