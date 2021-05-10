names = ["Colin", "Daniel", "Mariel", "Eva", "Katya"]

# print list with lengths of each name
print([len(name) for name in names])

# print even number names
print([name for name in names if (len(name) % 2) == 0])
