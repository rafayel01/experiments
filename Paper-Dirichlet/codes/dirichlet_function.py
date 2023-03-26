import numpy as np


def coef(k, l, beta):
    return sum((beta**s*(s+1)*(l+1) for s in range(k-l-1))) + sum((beta**s*(k-1-s)*(k-1-l) for s in range(k-1-l, k-1)))


def func(alpha, beta, n):
    return round(np.linalg.norm(sum([coef(n, m, beta)*alpha**m for m in range(n-1)])), 5)


def solve_numpy(n, beta):
  coeffs = np.array([coef(n, m, beta) for m in range(n-2, -1, -1)])
  roots = np.roots(coeffs)
  return roots


alpha = -0.09-0.63538529j # Set value of alpha
beta = complex(0.01, 0.1)  # Set value of beta
k = 5                       # Set k

print(solve_numpy(k, beta)) # When beta = beta and get values of alpha when function is equal to zero

print(func(alpha, beta, k))  # Get function values