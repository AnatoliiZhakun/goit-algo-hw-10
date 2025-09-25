import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x**2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок
N = 100000

# Знаходимо верхню межу для y (максимум функції на відрізку)
y_max = max(f(np.linspace(a, b, 100)))

# Генеруємо випадкові точки в прямокутнику [a, b] × [0, y_max]
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, y_max, N)

# Визначаємо, які точки потрапили під криву
points_under_curve = y_rand <= f(x_rand)

# Метод Монте-Карло: оцінка площі
integral_mc = (b - a) * y_max * np.sum(points_under_curve) / N
print("Інтеграл методом Монте-Карло:", integral_mc)

# Аналітичне обчислення інтеграла через scipy.quad
result, error = spi.quad(f, a, b)
print("Інтеграл через quad:", result, "±", error)

# Висновок про точність
accuracy = abs(integral_mc - result)
print("Різниця між методами:", accuracy)

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b, 100)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
