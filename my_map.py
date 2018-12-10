from functools import reduce

# Map takes a function and a collection of items. It makes a new, empty collection, runs the function on each item
# in the original collection and inserts each return value into the new collection. It returns the new collection.

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])
print(names)


names = ['Mary', 'Isla', 'Sam']

secret_names = map(hash, names)
print(secret_names)
