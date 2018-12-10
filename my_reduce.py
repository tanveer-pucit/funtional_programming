from functools import reduce

# Reduce takes a function and a collection of items. It returns a value that is created by combining the items.

summ = reduce(lambda a, vaiable: a + vaiable, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(summ)
