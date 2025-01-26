# Lists a and b
a = [1, 2, 3, 4]
b = [5, 6, 7]

# Creating the dictionary
result = {}
for i in a:
    for j in b:
        result[(i, j)] = i * j

# Printing the result
print(result)
