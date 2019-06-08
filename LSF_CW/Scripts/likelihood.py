import numpy as np
import matplotlib.pyplot as plt

def f(a, b, c, t):
    return a * np.sin(b * t) + c * np.log(t + 1)

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(7, 7))
ax = axs[0]

t1 = np.linspace(0, 10, 10)
a1 = 2
b1 = 0.5
c1 = 4
y1 = f(a1, b1, c1, t1) + np.random.uniform(-1, 1, 10)
ax.errorbar(t1, y1, yerr=1.5, fmt="o", label="data")

a2 = 2.1
b2 = 0.49
c2 = 4.05
t2 = np.linspace(0, 10, 100)
y2 = f(a2, b2, c2, t2)
ax.plot(t2, y2, label="model")
ax.legend()

ax = axs[1]
residuals = f(a2, b2, c2, t1) - y1

ax.stem(t1, residuals, label="residuals")
ax.legend()

plt.savefig("../Images/likelihood.png")
plt.show()
