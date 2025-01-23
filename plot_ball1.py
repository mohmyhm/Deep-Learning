import numpy as np
import matplotlib.pyplot as plt


def function(t, v0, g):
    return v0*t-0.5*g*(t**2)


v0 = 10
g = 9.81
T = np.linspace(0, 2*v0/g, 50)

plt.plot(T, function(T, v0, g), marker='x', color='b')

plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.title('plot_ball1.py')
plt.show()