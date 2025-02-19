animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
    animals = ['yellow tang', 'moorish idol', 'anemonefish']
for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animal))