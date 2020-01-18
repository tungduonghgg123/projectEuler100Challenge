# What is the some of the digits of 2^1000?

# Solution: calculate 2^1000 then pass it to string because of the supportted bit. Then make a loop through all its elements to acquire the sum.

from number import sumOfDigits

number = pow(2,1000)
print(sumOfDigits(number))