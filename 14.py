# Which starting number, under one million, produces the longest chain?

def nextNumber(n):
    if(n % 2 == 0):
        return n/2
    return 3 * n +1
def countTheChain(n):
    start = n 
    count = 1
    while(start != 1):
        start = nextNumber(start)
        count = count + 1
    return count
longestChain = 1
startNumber = 1
for x in range ( 1, pow(10,6)):
    count = countTheChain(x)
    if count > longestChain:
        longestChain = count
        startNumber = x
print(longestChain)
print(startNumber)