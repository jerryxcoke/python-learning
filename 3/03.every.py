NoMinusList = [2,66,44,-23,42]

isEvery = True
i = 0

while i < len(NoMinusList) and isEvery:
    if NoMinusList[i] < 0 :
        isEvery = False
    i = i + 1

if(isEvery):
    print('not every item is positive. found one negative at: ' + str(i))
else:
    print('Yea boi')