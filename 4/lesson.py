PetersAnimals = ["cat", "dog", "dragon", "turtle"]
myAnimals = ["turtle", "dyno", "elephant", "dog", "monkey"]

results = []

counter = 0

def isInList(lister, item):
    j = 0
    while j < len(lister) and item != lister[j]:
        j = j + 1
    return j < len(lister)

for animal in PetersAnimals:
    if isInList(myAnimals, animal):
        counter = counter + 1
        results.append(animal)


print(results)