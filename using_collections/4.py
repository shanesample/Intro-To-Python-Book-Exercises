pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])

x = pets.get('lizard')
print(x)

y = pets.get('lizard', 'silence!')
print(y)