# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

from number import number2word

def removeRedundant(word):
    # remove space and hyphen
    return word.replace(' ','').replace('-','')
letters = 0
for x in range ( 1, 1001):
    word = number2word(x)
    letters = letters + len(removeRedundant(word))
print(letters)