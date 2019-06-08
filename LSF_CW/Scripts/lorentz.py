import numpy as np
import matplotlib.pyplot as plt

c = 3.0e8

def galilean(t, x, v):
    return t, x - (v * t)

def lorentz(t, x, v):
    gamma = 1 / np.sqrt(1 - (v / c)**2)
    t_prime = gamma * (t - (v * x / c**2))
    x_prime = gamma * (x - (v * t))
    return t_prime, x_prime

t = np.linspace(0, 100, 100)
x = 0

v_c = 0.9
v = v_c * c

t_prime, x_prime = galilean(t, x, v)
plt.plot(t_prime, x_prime, label="Galilean")

t_prime, x_prime = lorentz(t, x, v)
plt.plot(t_prime, x_prime, label="Lorentz")

plt.legend()
plt.show()
