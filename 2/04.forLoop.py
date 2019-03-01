print("# print values sqr between 0 and 9")
for value in range(0,10):
    print(value * value)

print("# print every second value")
for value in range(0,10, 2):
    print(value * value)

print("# print number except when 2")
for value in range(0,11,2):
    if  value == 2:
        print('Two')
    else:
        print(value * value)

print("# divisible by 2 or 3")
for value in range(1,11):
    if  value % 2 == 0:
        print(value)
    else:
        if value % 3 == 0:
            print(value)