
# Solution: From the third row ahead, each internal number will acts as a child node of two father nodes right above it.
# This senario enables cutting branch when it is not neccessary to travel this child node two times ( each time from different path )

from number import readInput

input = readInput('67_input.txt')
totalRows = len(input)
maximumTotalToBottomDict = {}
countVisitedNode = 0

def outOfBound(x):
    if x > totalRows - 1:
        return True
    return False
def discovered(node):
    if maximumTotalToBottomDict.get(node):
        return True 
    return False
def travel(node):
    global countVisitedNode
    x = node[0]
    y = node[1]
    if(outOfBound(x)):
        return 0
    countVisitedNode = countVisitedNode + 1
    longestRoute = 0
    for i in range(0, 2):
        children = ( x + 1, y + i)
        if discovered(children): 
            longestRoute = max(longestRoute, maximumTotalToBottomDict.get(children))
        else:
            longestRoute = max(longestRoute, travel(children))
    maximumTotalToBottomDict.update({(x, y): input[x][y] + longestRoute})
    return maximumTotalToBottomDict.get((node))

root = (0, 0)
print('longest path:', travel(root))

print(countVisitedNode)
