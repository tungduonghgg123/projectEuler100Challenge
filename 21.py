from number import findDivisors, sumOfProperDivisors




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
