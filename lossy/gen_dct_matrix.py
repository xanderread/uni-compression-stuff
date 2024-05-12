import math

# Size of the DCT matrix
N = 4

# Function to compute C_i coefficient
def get_Ci(i, N):
    return math.sqrt(1 / N) if i == 0 else math.sqrt(2 / N)

# Initialize the DCT matrix
dct_matrix = [[0] * N for _ in range(N)]

# Fill the DCT matrix based on the given formula
for i in range(N):
    Ci = get_Ci(i, N)
    for j in range(N):
        dct_matrix[i][j] = Ci * math.cos((2 * j + 1) * i * math.pi / (2 * N))

# Print the resulting DCT matrix
for row in dct_matrix:
    print(row)
