import math

inputNumber = input('give me a number: ')
number = int(inputNumber)

toNumber = math.floor(int(number)/2+1)
for value in range(2,toNumber):
    if  number % value == 0:
        print(value)