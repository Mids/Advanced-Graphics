# Problem 1
# 2 to 26 array
M = list(range(2, 27))
print(M)

# Problem 2
# as a 5x5
M = [M[i:i + 5] for i in range(0, len(M), 5)]
print(M)

# Problem 3
# make inner value 0
for i in range(1, 4):
	for j in range(1, 4):
		M[i][j] = 0
print(M)

# Problem 4
# M^2
M2 = [[0 for i in range(5)] for j in range(5)]
for i in range(len(M)):
	for j in range(len(M[0])):
		for k in range(len(M)):
			M2[i][j] += M[i][k] * M[k][j]
M = M2
print(M)

# Problem 5
# magnitude of v in M
# use np.sqrt
import numpy as np

magnitude = np.sqrt(sum([np.square(M[0][i]) for i in range(5)]))
print(magnitude)