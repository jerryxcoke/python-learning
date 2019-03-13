def isInList(lister, elem) :
    j = 0
    while j < len(lister) and elem != lister[j]:
        j = j + 1
    return j < len(lister)

animals = ["cat", "dog", "dragon", "turtle"]
myAnimals = ["turtle", "dyno", "elephant", "dog", "monkey"]

results = []

counter = 0

for animal in animals:
    if isInList(myAnimals, animal):
        counter = counter + 1
        results.append(animal)


print(str(results))
