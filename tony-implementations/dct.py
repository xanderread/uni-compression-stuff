import numpy as np

matrix = [[10,3,5,1],
          [2,4,6,8],
          [12,7,0,0],
          [3,8,1,2]]

# Define the cosine matrix for the 2D DCT
C = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        if i == 0:
            C[i][j] = (1/2) * np.cos(((2*j + 1) * i * np.pi) / (2*4))
        else:
            C[i][j] = (np.sqrt(2)/2) * np.cos(((2*j + 1) * i * np.pi) / (2*4))

# Perform the 2D DCT on the matrix
dct = np.dot(np.dot(C, matrix), np.transpose(C))

# Set all values after the 3rd value in the zigzag order to 0
sum = 0
for i in range(4):
    for j in range(4):
        if i+j > 1:
            dct[i][j] = 0

# Perform the inverse 2D DCT on the matrix
inverse_dct = np.dot(np.dot(np.transpose(C), dct), C)

# Find the MSE
mse = np.mean((np.array(matrix) - np.array(inverse_dct))**2)

print(mse)