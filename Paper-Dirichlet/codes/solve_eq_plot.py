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


def plot_points_numpy(n, beta):
  center = (0, 0)
  radius = 1
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + radius*np.cos(theta)
  y = center[1] + radius*np.sin(theta)
  fig, ax = plt.subplots()
  ax.plot(x, y, label='r = 1')
  ax.set_aspect('equal', adjustable="datalim")
  solutions = solve_numpy(n, beta)
  print(solutions)
  real = solutions.real
  imag = solutions.imag
  ax.scatter(real, imag, c='r')
  plt.title(f"alpha  when beta = {round(beta, 2)}")
  plt.xlabel("Real")
  plt.ylabel("Imag")
  plt.show()


plt.style.use('seaborn-whitegrid')
k = 5
beta = np.linspace(-0.99, 0.99, 10)
print(beta)
for b in beta:
    for k_ in range(3, k+1):
        plot_points_numpy(k_, b)


