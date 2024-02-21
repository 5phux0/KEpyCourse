# Script rewritten using numpy
# Runs in 29 ms
import numpy as np

N = 250

# NxN matrix
X = np.random.randint(0, 100, [N, N])

# Nx(N+1) matrix
Y = np.random.randint(0, 100, [N, N+1])

# result is Nx(N+1)
result = np.matmul(X, Y)

rlist = result.tolist()
for r in rlist:
    print(r)
