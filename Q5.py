# Initialize a 3x3 matrix
matrix = []

# Input integers for the 3x3 matrix
print("Enter integers for the 3x3 matrix (row by row):")
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter value for matrix[{i+1}][{j+1}]: "))
        row.append(value)
    matrix.append(row)

# Initialize variables for results
row_sums = []
col_sums = [0] * 3
prod_main_diag = 1
prod_anti_diag = 1

# Calculate row sums, column sums, and diagonal products
for i in range(3):
    row_sum = 0
    for j in range(3):
        row_sum += matrix[i][j]
        col_sums[j] += matrix[i][j]
        # Main diagonal (i == j)
        if i == j:
            prod_main_diag *= matrix[i][j]
        # Anti-diagonal (i + j == 2)
        if i + j == 2:
            prod_anti_diag *= matrix[i][j]
    row_sums.append(row_sum)

# Calculate the total sum of rows and columns
total_row_sum = sum(row_sums)
total_col_sum = sum(col_sums)

# Store results in a dictionary
results = {
    'sumR': total_row_sum,
    'sumC': total_col_sum,
    'prodR': prod_main_diag,
    'prodL': prod_anti_diag
}

# Display the results
print("\nMatrix:")
for row in matrix:
    print(row)

print("\nResult:", results)
