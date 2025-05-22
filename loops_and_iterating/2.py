"""
age = int(input('how old are you?'))

print(f'you are {age} years old.')
print(f'in 10 years you will be {age + 10} years old.')
print(f'in 20 years you will be {age + 20} years old.')
print(f'in 30 years you will be {age + 30} years old.')
print(f'in 40 years you will be {age + 40} years old.')
"""

age = int(input('how old are you'))
print(f'you are {age} years old.')
years = 10
for i in range(1, 6):
    print(f'in {years} years you will be {age + years} years old.')
    years += 10