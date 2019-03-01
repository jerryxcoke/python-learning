myList = [2,66,44,23,42]

maxValue = myList[0]
maxIndex = 0

for index in range(0,4):
    if(maxValue < myList[index]):
        maxValue = myList[index]
        maxIndex = index

print(maxValue)

#better ------------------------
myList = [2,66,44,23,42]

maxValue = myList[0]
maxIndex = 0

for index in range(1,len(myList)):
    if(maxValue < myList[index]):
        maxValue = myList[index]
        maxIndex = index

print(maxValue)