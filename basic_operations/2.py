num = 4936

ones = num % 10
print(ones) # 6

num = (num // 10)
print(num)

tens = num % 10
print(tens) // 3

num = num // 10
print(num)

hundreds = num % 10
print(hundreds) // 9
print(num)

thousands = (num // 10)
print(thousands) // 4
