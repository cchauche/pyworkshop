import pprint
import random

names = ["Colin", "Daniel", "Mariel", "Eva", "Katya"]

# print list with lengths of each name
print([len(name) for name in names])

# print even number names
print([name for name in names if (len(name) % 2) == 0])

# Create a list of odd numbers between 0 and 100
pprint.pprint([num for num in range(0,100) if num % 2])

# Create dictionary with even keys and random in values
even_dict = {num:random.randint(0,100) for num in range(0,100) if not num % 2}
pprint.pprint(even_dict)

# Create set of values from above dictionary
my_set = {num for num in even_dict.values()}
pprint.pprint(my_set)
print(len(my_set))