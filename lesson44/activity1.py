# tuple and set
a = (94, 85, 69, 34, 23, 11, 16, 20)

print(a)
print(type(a))

print(a[0])
print(a[3])
print(a[5])

print(a[1:5])

for i in range(0, len(a)):
    print(f'The {i} element of a is {a[i]}')

# a[0] = 194 not possible with tuple since tuple is immutable

b = ('aadhya', 'singh', 'soumil', 85, True, 0.32, [23, 234, 545, 4645], ('asdf', '23', 323, False))

print(b[6][2])


# sets data structure now
c = {1, 3, 3, 3, 8, 5, 0, 1, 3, 9}
print(c)

c.add(12)
print(c)

# print(c[2]) it is going through the error bcz sets are inaccessable

d = {23, 2, 2, 3, 1, 0, 6, 8, 9}

print(c.difference(d))
print(c.symmetric_difference(d))
print(c.union(d))
print(c.intersection(d))
