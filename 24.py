# What is the millionth lexicographic permutation of the digits from 0 to 9

digits = [0,1,2,3,4,5,6,7,8,9]

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
    print(generatePermutionsRecurively(digits)[index])
def secondApproach(digits):
    # using mathematically method, get the result quicker
    pass
index = pow(10, 6) - 1
firstApproach(digits, index)
# print(generatePermutionsRecurively())