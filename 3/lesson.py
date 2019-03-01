# http://progalap.elte.hu/?El%C5%91ad%C3%A1s


#find max
temps = [23,0, -3, 34, 7, 23, 0]

tempsLength = len(temps)

maxIndex = 0

for i in range(1,tempsLength):
    if temps[i] > temps[maxIndex]:
        maxIndex = i

print(temps[maxIndex])