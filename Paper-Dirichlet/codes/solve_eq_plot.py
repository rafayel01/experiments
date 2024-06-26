import numpy as np
import matplotlib.pyplot as plt

colors = ('cyan', 'palegreen', 'Red', 'Blue', 'crimson', 'Orange', 'Black', 'Yellow',\
          'Purple', 'Silver', 'Brown', 'Gray', 'Pink', 'Olive',\
          'Maroon', 'Violet', 'Magenta', 'Green')

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


#print(solve_numpy(16, 0.2-0.8j))

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


def plot_points_numpy_together(n, beta, save=False):
  markers = ('^', 'o', '*', 'd' ,'s')
  center = (0, 0)
  radius = 1
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + radius*np.cos(theta)
  y = center[1] + radius*np.sin(theta)
  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.set_aspect('equal', adjustable="datalim")
  for i in n:
    solutions = solve_numpy(i, beta)
    real = solutions.real
    imag = solutions.imag
    ax.scatter(real, imag, c='black', label=f'k = {i}', marker=markers[np.where(k==i)[0][0]])
  #if beta.imag == 0:
  #  plt.title(f"\u03B2 = {round(beta.real, 2)}")
  #else:
  #  plt.title(f"\u03B2 = {round(beta, 2)}")
  plt.xlabel("Real")
  plt.ylabel("Imag")
  plt.legend(fontsize=9.5)
  #plt.show()
  if save:
    plt.savefig(f"beta_{round(beta, 2)}_k_{n}.png")


def plot_points_numpy_together_onefig(n, beta, save=False):
  markers = ('^', 'o', '*', 'd' ,'s')
  center = (0, 0)
  radius = 1
  theta = np.linspace(0, 2*np.pi, 100)
  x = center[0] + radius*np.cos(theta)
  y = center[1] + radius*np.sin(theta)
  fig, ax = plt.subplots(1, 2, figsize=(12, 4))
  for j in range(2):
    ax[j].plot(x, y)
    ax[j].set_aspect('equal', adjustable="datalim")
    for i in n:
      solutions = solve_numpy(i, beta[j])
      real = solutions.real
      imag = solutions.imag
      ax[j].scatter(real, imag, c='black', label=f'k = {i}', marker=markers[np.where(k==i)[0][0]])
      if beta[j].imag == 0:
        ax[j].set_title(f"\u03B2 = {round(beta[j].real, 2)}")
      else:
        ax[j].set_title(f"\u03B2 = ({round(beta[j].real, 2)} + {round(beta[j].imag, 2)}i)")
      ax[j].set(xlabel = "Real", ylabel = "Imag")
      ax[j].set_xlim(-1.5, 1.5)
      ax[j].set_ylim(-1, 1)
      ax[j].legend(fontsize=8, loc='upper right')
  plt.tight_layout()
  if save:
    plt.savefig(f"beta_{beta}_k_{n}_together.png")


plt.style.use('seaborn-whitegrid')
#k = 5
beta = np.array([0.2+0.3j, 0.4+0.5j]) #np.linspace(-0.99, 0.99, 10)
#k = [3, 5, 10, 20, 50]
k = np.array([3, 8, 15, 30])
#plot_points_numpy_together_onefig(k, beta, save=True)
#for b in beta:
#  plot_points_numpy_together(k, b, save=True)
plot_points_numpy_together(k, beta=0, save=True)

