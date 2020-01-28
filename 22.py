def readInput():
    f = open('22_names.txt', 'r')
    names = f.readline()
    def format(input):
        input = input.split(',')
        output = []
        for name in input:
            output.append(name.replace('"',''))
        return output
    return format(names)


def convertAlphabetLetter2Number(letter):
    # number in the alphabetical order ( 1,2,..,26)
    padding = ord('A') - 1
    return ord(letter.upper()) - padding

def isBehind(word1, word2):
    # if word1 is behind word2 then return TRUE, else return FALSE
    length1 = len(word1)
    length2 = len(word2)
    shorterLength = min(length1, length2)
    count = 1
    while(count <= shorterLength):
        index = count - 1
        order1 = convertAlphabetLetter2Number(word1[index])
        order2 = convertAlphabetLetter2Number(word2[index])
        if order1 > order2:
            return True
        if order1 < order2:
            return False
        count += 1
    if length1 > length2:
        return True
    return False
def sortWordsIntoAlphabeticalOrder(words):
    size = len(words)
    count = 0
    while count < size:
        for i in range ( 0, size - count - 1):
            if isBehind(words[i], words[i+1]):
                words[i], words[i+1] = words[i+1], words[i]
        count += 1
    return words

def convertWord2Score(word):
    score = 0
    for letter in word:
        score += convertAlphabetLetter2Number(letter)
    return score

def calculateTotalNameScores(names):
    total = 0
    for index, name in enumerate( names, 1 ):
        total += convertWord2Score(name) * index
    return total
input = readInput()
sortedInput = sortWordsIntoAlphabeticalOrder(input)
print(calculateTotalNameScores(sortedInput))
