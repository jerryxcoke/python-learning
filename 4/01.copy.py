animals = ["cat", "dog", "dragon", "turtle"]
animalNameSizes = []

for animal in animals:
    animals.append(len(animal))

print(str(animalNameSizes))



#copy in copy
animals = ["cat", "dog", "dragon", "turtle"]
animal_reversed = []

for animal in animals:
    name = ''
    for i in range(len(animal), 0, -1):
        name += animal[i-1]
    animal_reversed.append(name)

print(str(animal_reversed))