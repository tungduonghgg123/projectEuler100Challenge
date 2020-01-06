# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit number.

def palindrome(num) :
    length = len(str(num))    
    if( length % 2 == 0 ):
        tail = int( num % pow( 10, length / 2 ) )
        head = int( num / pow( 10, length / 2 ))
        #TODO: reverse tail or head
        reverseTail = int(str(tail)[::-1])
        if( reverseTail - head == 0):
            return True
        return False
    else:
        tail = int( num % pow( 10, int( length / 2 )) )
        head = int  ( num / pow( 10, int( length / 2 + 1 )))
        reverseTail = int(str(tail)[::-1])
        if( reverseTail - head == 0):
            return True
        return False 
def findPalindrome():
    palindromes = []
    for x in range ( 999, 99, -1):
        for y in range ( 999, 99, -1):
            if( palindrome( x * y )):
                palindromes.append( x * y )
    print(max(palindromes))
findPalindrome()
