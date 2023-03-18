import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy
from scipy.optimize import fsolve
from scipy.optimize import root
import time

# Solve with sympy
def create_solve_eq(beta, k):
  def coef(k, j):
    return sum(m*beta**m for m in range(k)) - j*sum(beta**m for m in range(k))
  a = sympy.Symbol('a')
  eq = (coef(k, j)*a**j for j in range(k))
  eqt = 0
  for i in range(k):
    eqt += next(eq)
  eqt /= (a - beta)
  print(f'f = {eqt}')
  solutions = sympy.solve(eqt, a)
  return solutions



# Solve with scipy

def coef(k, j):
    return sum(m*0.25**m for m in range(k)) - j*sum(0.25**m for m in range(k))


def func(a):
  eq = sum((coef(3, j)*a**j for j in range(20)))
  return eq

'''
#Check time with scipy
start = time.time()
print(root(func, [-1-1j, 1+1j], method='hybr').x)
end_ = time.time()
print(end_-start)

#Check time with sympy
start = time.time()
print(create_solve_eq(0.25, 11))
end_ = time.time()
print(end_-start)
'''

# Input beta
beta = 0.25
results = []
# Input n
n = 10
for i in range(3, n + 1):
    print(f'i = {i}')
    res = create_solve_eq(beta, i)
    results.append(res)

if_equal = []
for i in range(len(results) - 1):
    for j in range(i+1, len(results)):
        for k in range(len(results[i])):
            for l in range(len(results[j])):
                if results[i][k] == results[j][l]:      # abs(results[i][k] - results[j][l]) < 10e-5:
                    print(results[i][k], results[j][l], "Equal")
                    if_equal.append((i, k))
                    break

if not if_equal:
  print("OK: no element when equal to 0 for another k")

print(results)
