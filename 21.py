from number import findDivisors


def sumOfProperDivisors(number):
    # numbers less than n which divide evenly into n
    sum = 0
    divisors = findDivisors(number)
    for divisor in divisors:
        sum += divisor
    return sum - number


def findAmicableNumbersUnder(limit):
    def amicableNumber(_num, _sum):
        for number, theSum in number2SumOfItsProperDivisors_Dict.items():
            if number == _sum and theSum == _num and number != _num:
                return True
        return False
        
    number2SumOfItsProperDivisors_Dict = {}
    amicableNumbers = []

    for num in range(limit):
        number2SumOfItsProperDivisors_Dict.update(
            {num: sumOfProperDivisors(num)})


    for number, theSum in number2SumOfItsProperDivisors_Dict.items():
        if amicableNumber(number, theSum):
            amicableNumbers.append(number)
    return sum(amicableNumbers)


print(findAmicableNumbersUnder(10000))
