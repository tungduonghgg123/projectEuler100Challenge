# What is the millionth lexicographic permutation of the digits from 0 to 9
from helper import toString
from math import factorial, ceil

def generatePermutionsRecurively(digits):
    results = []
    for index, digit in enumerate(digits):
        if len(digits) == 1:
            return [digit]
        digits.remove(digit)
        tails = generatePermutionsRecurively(digits)
        for tail in tails:
            results.append(str(digit) + str(tail))
        digits.insert(index, digit)
    return results
def firstApproach(digits, index):
    # 18 seconds
    print(generatePermutionsRecurively(digits)[index-1])
def generatePermutionsByBacktracking(digits, start, finish):
    if start == finish:
        return print(toString(digits))
    else:
        for i in range (start, finish + 1):
            digits[i], digits[start] = digits[start], digits[i]
            generatePermutionsByBacktracking(digits, start + 1, finish)
            digits[i], digits[start] = digits[start], digits[i]
            

def secondApproach(digits):
    # too slow and does not follow the order.
    generatePermutionsByBacktracking(digits, start = 0, finish = len(digits) - 1)
def thirdApproach(digits, index):
    # using mathematically method, get the result quicker. An the fact shows that it was true, less than a second execution time.
    length = len(digits)
    permutation = ''
    loopTurn = 0
    while(loopTurn < length ):
        # each loop we will get a digit of the desired permutation, from left to right
        subPages = factorial(length - loopTurn - 1) 
        page = ceil(index/subPages)
        print('page: ',page)
        index = index%subPages
        if index == 0:
            # because index of a page will be counted from 1, so index 0 is equal to the last index of a page
            lastIndex = length - loopTurn - 1  
            index = lastIndex
        print('index in that page:', index)
        print(digits)
        # page - 1 because index of an array starts from 0
        permutation += str(digits[page-1])
        del digits[page-1]
        
        loopTurn += 1
        print('----', permutation)
    print('result: ',permutation)

digits = [0,1,2,3,4,5,6,7,8,9]
index = pow(10,6)
# firstApproach(digits, index)
# secondApproach(list('0123456789'))
thirdApproach(digits, index)
# print(generatePermutionsRecurively(testDigits))
# 2783915460