animals = ["cat", "dog", "dragon", "turtle"]
myAnimals = ["turtle", "dyno", "elephant", "dog", "monkey"]

results = []

counter = 0

for animal in animals:
    j = 0
    while j < len(myAnimals) and animal != myAnimals[j]:
        j = j + 1
    if j < len(myAnimals):
        counter = counter + 1
        results.append(animal)


print(str(results))
