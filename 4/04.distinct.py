def isInList(listem, elem) :
    j = 0
    while j < len(listem) and elem != listem.keys()[j]:
        j = j + 1
    return j < len(listem)

animalWeights = {'fluffy': 425, 'dogee': 3452, 'sanyi': 2732, "csillag":113854}
myAnimals = list(['fluffy', 'sanyi'])
results = []

counter = 0

for animal in animalWeights:
    if isInList(myAnimals, animal):
        counter = counter + 1
        results.append(animal)


print(str(results))
