myList = [2,66,44,-23,42]

isFound = False
i = -1

while i < len(myList) and not isFound:
    if myList[i] < 0 :
        isFound = True
    i = i + 1

if(isFound):
    print('found negative at: ' + str(i))
    print('value: ' + str(myList[i]))
else:
    print('Yea boi')


