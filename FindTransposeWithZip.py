

#starting with a matrix
matrix = [[1,2,3],[1,2,3]]

#uses a for loop to combine matrix
matrix_transpose = [list(i) for i in zip(*matrix)]

#print transpose
print(matrix_transpose)

