# Calculate sum of the squares of the first one hundred natural number
sum1 = 0
for x in range ( 1, 101 ):
    sum1 += x * x

#Calculate the square of the sum
sum = ( 1 + 100 ) * 100 / 2
sum2 = sum * sum

print(int( sum2 - sum1 ))