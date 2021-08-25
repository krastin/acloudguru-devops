#!/usr/bin/env python3

# Strings
print("Strings:")
print('single quoted string')
print("double quoted string")

print('''
multi
line
string
''')

print('string' + 'arithmetic')
print('multiply' * 4)
print('abcde'.find('c'))
print('LoWeRCaSe'.lower())
print("Single\slash")
print("Double\\slash")

# Numbers
print("Numbers:")
print(2 + 2)
print(10 - 4)
print(5 / 3)
print(5 // 3)
print(5 % 3)
print(2 ** 3)
print(pow(2,3))
print(1.1 + 3)
print(float('7.0') + 1)
# print(int('1.1)) # error, can't typecast into int
print(int(5.5))

# Booleans and None
print("Booleans and None:")
print(None, True, False, bool(1.0))

# Variables
print("Variables:")
greeting = "Hello"
print(greeting)
greeting += " World!"
print(greeting)

# Lists
print("Lists:")
my_list = [1,2,3,4,5]
print(my_list)
print(my_list[3])
print(my_list[len(my_list) - 1])
print(my_list[0:2])
print(my_list[0:len(my_list):2])
my_list[0] = "a"
print(my_list)
print(my_list.pop())
my_list.append(6)
print(my_list)

# Tuples and Ranges
print("Tuples and Ranges:")
point = (2.0, 3.0)
# point[0] = 1.0 # cannot modify tuples
point_3d = point + (4.0,)
x, y, z = point_3d
print("My point coordinates are: %s and %s" % (point[0], point[1]))
print(range(10))
print(list(range(0, 10)))

# Dictionaries
print("Dictionaries:")
ages = { 'kevin': 29, 'alex': 29, 'bob': 40 }
print(ages)
ages['Keith'] = 29
print(ages)
del ages['Keith']
print(ages)
