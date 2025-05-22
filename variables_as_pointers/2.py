set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# set2 will now reference the same object(a set) in memory. So it will print out set1 values but maybe in a different order