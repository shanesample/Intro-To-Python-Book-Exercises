my_list = [6, 3, 0, 11, 20, 4, 17]
#Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.

"""
i = 0
while i < len(my_list):
    num = my_list[i]
    if num % 2 == 0:
        print(num)
    i+=1
"""

for i in my_list:
    if i % 2 == 0:
        print(i)

