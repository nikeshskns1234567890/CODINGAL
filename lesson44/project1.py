# Nikesh's details using Tuple and Set

# Tuple example (immutable data)
a = (94, 85, 69, 34, 23, 11, 16, 20)

print(a)
print(type(a))

print(a[0])
print(a[3])
print(a[5])

print(a[1:5])

for i in range(0, len(a)):
    print(f'The {i} element of a is {a[i]}')

# Nested tuple example
b = ('Nikesh', 14, 167, 49, [23, 234, 545, 4645], ('Badminton', 'Novels', 'Sports', 'Reading'))
print("One of my favorite hobbies is:", b[5][1])

# Set example (unique values, unordered)
c = {1, 3, 3, 3, 8, 5, 0, 1, 3, 9}
print("Original set c:", c)

c.add(12)
print("After adding 12:", c)

# Another set
d = {23, 2, 2, 3, 1, 0, 6, 8, 9}

print("Difference:", c.difference(d))
print("Symmetric Difference:", c.symmetric_difference(d))
print("Union:", c.union(d))
print("Intersection:", c.intersection(d))

# Personal details stored in dictionary
my_dict = {
    'name': 'Nikesh',
    'age': 14,
    'height_cm': 167,
    'weight_kg': 49,
    'hobbies': {'Novels', 'Reading', 'Sports', 'Badminton'}
}

print("\n--- My Details ---")
for key, value in my_dict.items():
    print(f"{key} : {value}")
