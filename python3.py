import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2):
    return 0.5 * (x1**4 - 16*x1**2 + 5*x1 + x2**4 - 16*x2**2 + 5*x2)

x1_min, x1_max = -5.0, 5.0
x2_min, x2_max = -5.0, 5.0
step = 0.1
test_point = (2.903534, -2.903534)

x1 = np.arange(x1_min, x1_max + step, step)
x2 = np.arange(x2_min, x2_max + step, step)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

test_value = f(test_point[0], test_point[1])

fig = plt.figure(figsize=(16, 12))
fig.suptitle(f'Функция: f(x1,x2) = 0.5(x1⁴-16x1²+5x1 + x2⁴-16x2²+5x2)\n'
             f'Тестовая точка: ({test_point[0]:.3f}, {test_point[1]:.3f}), '
             f'Значение: {test_value:.3f}', fontsize=14)

ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(X1, X2, Y, cmap='viridis', edgecolor='none')
ax1.set_title('3D поверхность (изометрический вид)')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('f(x1, x2)')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

ax2 = fig.add_subplot(222)
contour = ax2.contourf(X1, X2, Y, levels=20, cmap='viridis')
ax2.set_title('Вид сверху (проекция на плоскость X1X2)')
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
fig.colorbar(contour, ax=ax2, shrink=0.5, aspect=5)

ax3 = fig.add_subplot(223)
x2_fixed = test_point[1]
y_fixed_x2 = f(x1, x2_fixed)
ax3.plot(x1, y_fixed_x2, 'b-', linewidth=2)
ax3.set_title(f'График при x2 = {x2_fixed:.3f}')
ax3.set_xlabel('x1')
ax3.set_ylabel('f(x1, x2)')
ax3.grid(True)

ax4 = fig.add_subplot(224)
x1_fixed = test_point[0]
y_fixed_x1 = f(x1_fixed, x2)
ax4.plot(x2, y_fixed_x1, 'r-', linewidth=2)
ax4.set_title(f'График при x1 = {x1_fixed:.3f}')
ax4.set_xlabel('x2')
ax4.set_ylabel('f(x1, x2)')
ax4.grid(True)

plt.tight_layout()
plt.show()