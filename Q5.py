# Initialize a 3x3 matrix
matrix = []

# Input integers for the 3x3 matrix
print("Enter integers for the 3x3 matrix (row by row):")
for i in range(3):
    row = []
    for j in range(3):
        # value = int(input(f"Enter value for matrix[{i+1}][{j+1}]: "))
        value = int(input())
        # row.append(value)
        row+=[value];
    # matrix.append(row)
    matrix+=[row]

# Initialize variables for results
row_sums = []
col_sums = []
prod_main_diag = 1
prod_anti_diag = 1

for i in range(3):
    r,c=0,0
    for j in range(3):
        r+=matrix[i][j]
        c+=matrix[j][i]
    row_sums+=[r]
    col_sums+=[c]

prodL,prodR=1,1
for i in range(3):
    prodL*=matrix[i][i]
    prodR*=matrix[2-i][i]

d={}
d['SumR1']=row_sums[0]
d['SumR2']=row_sums[1]
d['SumR3']=row_sums[2]
d['SumC1']=col_sums[0]
d['SumC2']=col_sums[1]
d['SumC3']=col_sums[2]
d['ProdL']=prodL
d['ProdR']=prodR

print (d)

# Calculate row sums, column sums, and diagonal products
# for i in range(3):
#     row_sum = 0
#     for j in range(3):
#         row_sum += matrix[i][j]
#         col_sums[j] += matrix[i][j]
#         # Main diagonal (i == j)
#         if i == j:
#             prod_main_diag *= matrix[i][j]
#         # Anti-diagonal (i + j == 2)
#         if i + j == 2:
#             prod_anti_diag *= matrix[i][j]
#     row_sums.append(row_sum)

# Calculate the total sum of rows and columns
# total_row_sum = sum(row_sums)
# total_col_sum = sum(col_sums)

# # Store results in a dictionary
# results = {
#     'sumR': total_row_sum,
#     'sumC': total_col_sum,
#     'prodR': prod_main_diag,
#     'prodL': prod_anti_diag
# }

# # Display the results
# print("\nMatrix:")
# for row in matrix:
#     print(row)

# print("\nResult:", results)
