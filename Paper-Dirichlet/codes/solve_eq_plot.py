import numpy as np
import matplotlib.pyplot as plt


def coef(k, l, beta):
    return sum((beta**s*(s+1)*(l+1) for s in range(k-l-1))) + sum((beta**s*(k-1-s)*(k-1-l) for s in range(k-1-l, k-1)))
    #for s in range(k-l-1):
    #    print(s, (s+1)*(l+1)*beta**s)
    #print(sum(((s+1)*(l+1)*beta**s for s in range(k-l-1))))
    #print(sum(((k-1-s)*(k-1-l)*beta**s for s in range(k-1-l, k-1))))


def solve_numpy(n, beta):
  coeffs = np.array([coef(n, m, beta) for m in range(n-2, -1, -1)])
  roots = np.roots(coeffs)
  return roots


def plot_points_numpy(n, beta, save=False):
  center = (0, 0)
  radius = 1
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + radius*np.cos(theta)
  y = center[1] + radius*np.sin(theta)
  fig, ax = plt.subplots()
  ax.plot(x, y, label='r = 1')
  ax.set_aspect('equal', adjustable="datalim")
  solutions = solve_numpy(n, beta)
  real = solutions.real
  imag = solutions.imag
  ax.scatter(real, imag, c='r', label=f'\u03B2 = {beta}, k = {n}')
  plt.title(f"\u03B1  when \u03B2 = {round(beta, 2)}, k = {n}")
  plt.xlabel("Real")
  plt.ylabel("Imag")
  if save:
    plt.savefig(f"/home/rafayel/experiments/Paper-Dirichlet/codes/plots/beta_{round(beta, 2)}_k_{n}.jpeg")

plt.style.use('seaborn-whitegrid')
#k = 5
beta = np.linspace(-0.99, 0.99, 10)
k = [3, 5, 10, 20, 50]
for b in beta:
    for k_ in k:
        plot_points_numpy(k_, b, save=True)


