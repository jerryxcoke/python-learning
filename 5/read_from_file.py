
# every line contains 1 integer
sum = 0
with open('5/helloka.txt') as openfileobject:
    for line in openfileobject:
       sum += int(line)
print(sum)


# into dictonary  key - value pair
commands = {}
filename = '5/commands.txt'
with open(filename) as fh:
    for line in fh:
        command, description = line.strip().split(' ', 1)
        commands[command] = description.strip()
print(commands)