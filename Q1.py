# Sample input dictionary D1
# D1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
D1={}
n=int(input('Enter number of keys for D1: '))
for i in range(n):
    key=input('Enter key: ')
    m=int(input('Enter number of elements in the List:  '))
    l = ['m']*m
    for i in range(m):
        l[i]=int(input(''))

    D1[key]=l  


# Create an empty dictionary D2
D2 = {}

# Loop through each key-value pair in D1
for key in D1:
    total = 0  # Initialize total sum to 0 for each key
    for number in D1[key]:  # Loop through each number in the list
        total = total + number  # Add the number to total
    D2[key] = total  # Store the total in D2 under the same key

# Print the result dictionary D2
print(D2)

