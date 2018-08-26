import numpy as np
import matplotlib.pyplot as plt

# squares = [0, 1, 4, 9, 16, 25]
# plt.plot(squares, c='red', linewidth=5)

x_values = list(range(10+1))
x_len = len(x_values)-1
y_values = list(x**2 for x in x_values)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolor='none', s=40)

plt.title("Square Numbers", fontsize=22)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of Value", fontsize=16)


plt.tick_params(axis="both", which='major', \
    labelsize=12, length=6, width=2, colors=(0, 0.8, 0), \
    grid_alpha=0.5, grid_color=(0, 1, 0, 0), direction='out')
plt.xticks(np.arange(min(x_values), max(x_values)+1, x_len/10))
plt.yticks(np.arange(min(y_values), max(y_values)+1, x_len**2/10))
plt.grid()

plt.savefig('squares_plot.png')
plt.show()
