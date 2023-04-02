import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import sympy


colors = ('cyan', 'palegreen', 'Red', 'Blue', 'crimson', 'Orange', 'Black', 'Yellow',\
          'Purple', 'Silver', 'Brown', 'Gray', 'Pink', 'Olive',\
          'Maroon', 'Violet', 'Magenta', 'Green')



def create_solve_eq(n):
  a = sympy.Symbol('a')
  eq = ((m+1)*a**m for m in range(n))
  eqt = 0
  for i in range(n):
    eqt += next(eq)
  print(eqt)
  solutions = sympy.solve(eqt, a)
  return solutions


def plot_points(n, save=False):
  center = (0, 0)
  radius = 1
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + radius*np.cos(theta)
  y = center[1] + radius*np.sin(theta)
  fig, ax = plt.subplots()
  ax.plot(x, y)# , label='r = 1')
  ax.set_aspect('equal', adjustable="datalim")
  ax.set_xlim(-1.5, 1.5)
  ax.set_ylim(-1.5, 1.5)
  solutions = create_solve_eq(n)
  points_real = []
  points_imag = []
  for j in range(len(solutions)):
    points_real.append(complex(solutions[j]).real)
    points_imag.append(complex(solutions[j]).imag)
  ax.scatter(points_real, points_imag, c='r', label=f'k={n}')
  #plt.title(f"alpha  when m = {n}")
  plt.xlabel("Real")
  plt.ylabel("Imag")
  plt.legend(loc='upper right', title_fontsize='xx-small', frameon=False)
  if save:
    plt.savefig(f'k_{n}.png')
  #plt.show()


def plot_points_together(n, save = False):
  center = (0, 0)
  radius = 1
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + radius*np.cos(theta)
  y = center[1] + radius*np.sin(theta)
  fig, ax = plt.subplots()
  ax.plot(x, y)# , label='r = 1')
  ax.set_aspect('equal', adjustable="datalim")
  ax.set_xlim(-1.5, 1.5)
  ax.set_ylim(-1.5, 1.5)
  for i in range(3, n + 1):
    print(f'k = {i}')
    solutions = create_solve_eq(i)
    points_real = []
    points_imag = []
    for j in range(len(solutions)):
      points_real.append(complex(solutions[j]).real)
      points_imag.append(complex(solutions[j]).imag)
    ax.scatter(points_real, points_imag, c=colors[i-3], label=f'k={i}')
  #plt.title(f"alpha  when m = {n}")
  plt.xlabel("Real")
  plt.ylabel("Imag")
  plt.legend(loc='upper right', title_fontsize='xx-small', frameon=False)
  if save:
    plt.savefig(f'k_{n}_together.png')
  plt.show()


def solve_numpy(n):
  coeffs = np.array([(m+1) for m in range(n-1, -1, -1)])
  roots = np.roots(coeffs)
  return roots


def plot_points_numpy(n):
  center = (0, 0)
  radius = 1
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + radius*np.cos(theta)
  y = center[1] + radius*np.sin(theta)
  fig, ax = plt.subplots()
  ax.plot(x, y, label='r = 1')
  ax.set_aspect('equal', adjustable="datalim")
  solutions = solve_numpy(n)
  real = solutions.real
  imag = solutions.imag
  ax.scatter(real, imag, c='r')
  plt.title(f"alpha  when m = {n}")
  plt.xlabel("Real")
  plt.ylabel("Imag")
  plt.show()

def plot_points_numpy_together(n, save=False):
  markers = ('^', 'o', '*', 'd' ,'s')
  center = (0, 0)
  radius = 1
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + radius*np.cos(theta)
  y = center[1] + radius*np.sin(theta)
  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.set_aspect('equal', adjustable="datalim")
  ax.set_xlim(-1.5, 1.5)
  ax.set_ylim(-1.5, 1.5)
  print(n)
  for i in n:
    solutions = solve_numpy(i)
    real = solutions.real
    imag = solutions.imag
    ax.scatter(real, imag, c='black', label=f'k={i}', marker=markers[np.where(k==i)[0][0]])
  plt.title(f"")
  plt.xlabel("Real")
  plt.ylabel("Imag")
  plt.legend(loc='upper right', fontsize=9.5, frameon=False)
  #plt.show()
  if save:
    plt.savefig(f'k_{n}_together.png')

plt.style.use('seaborn-whitegrid')

k = np.array([3, 8, 15, 30])
plot_points_numpy_together(k, save=True)

#create_solve_eq(3)

#plot_points_numpy(100)

#plot_points_numpy_together(20, False)

#plot_points_numpy_together(20)
