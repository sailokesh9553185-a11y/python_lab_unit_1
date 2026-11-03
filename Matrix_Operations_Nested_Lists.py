# Unit-3A_Task-5_Matrix_Operations_Nested_Lists.py
# Program to perform matrix addition using nested lists

# Defining two 3x3 matrices
matrix_a = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_b = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

# Initializing a result matrix with zeros
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Performing Matrix Addition
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

# Displaying the matrices
print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

print("\nResultant Matrix (Addition):")
for row in result:
    print(row)
