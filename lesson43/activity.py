fruits = ['Apple', 'Mango', 'Banana', "Strawberry", 'Soumil']

print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[4])
print(fruits[len(fruits) - 1])
print(fruits[-1])
print(fruits[-2])

print(fruits[2:4])
print(fruits[0:4:1])

 # fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)

fruits.append('aadhya')
print(fruits)

fruits.pop()
print(fruits)

fruits.remove('Mango')
print(fruits)

my_dict = {'name': 'krsna', 'age': 5000, 'location': 'Mathura'}

print(my_dict)
print(my_dict['age'])
# print(my_dict.age) this will give you error

print(len(my_dict))

my_dict['age'] = 10000
print(my_dict)

my_dict.pop('age')
print(my_dict)
