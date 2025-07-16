import numpy as np
import matplotlib.pyplot as plt
import json
import os

def f(x):
    return np.sin(3 * np.pi * x)**3 + (x - 1)**2 * (1 + np.sin(3 * np.pi)**2)

x_min = -10
x_max = 10
step = 0.01

x_values = np.arange(x_min, x_max + step, step)
y_values = f(x_values)

if not os.path.exists('results'):
    os.makedirs('results')

data = {
    "x": x_values.tolist(),
    "y": y_values.tolist()
}

with open('results/function_data.json', 'w') as file:
    json.dump(data, file, indent=4)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = sin³(3πx) + (x-1)²(1+sin²(3π))', color='blue')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.savefig('results/function_plot.png')
plt.show()