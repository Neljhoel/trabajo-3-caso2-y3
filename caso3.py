import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones
x = sp.symbols('x')
g = x**2 + x + 1  # g(x)
f1 = x**2         # f(x) = x^2
f2 = x            # f(x) = x

# Función para comprobar si g(x) es O(f(x))
def is_O(g, f, x0=1):
    limit_g = sp.limit(g / f, x, sp.oo)
    if limit_g.is_infinite:
        return False
    return limit_g < sp.oo

# Verificar O(x^2)
result_O_x2 = is_O(g, f1)
print(f"g(x) = x^2 + x + 1 es O(x^2): {result_O_x2}")

# Verificar O(x)
result_O_x = is_O(g, f2)
print(f"g(x) = x^2 + x + 1 es O(x): {result_O_x}")

# Gráfica
x_vals = np.linspace(0, 10, 400)  # Rango de x
g_vals = [g.subs(x, val) for val in x_vals]  # Evaluación de g(x)
f1_vals = [f1.subs(x, val) for val in x_vals]  # Evaluación de f(x) = x^2
f2_vals = [f2.subs(x, val) for val in x_vals]  # Evaluación de f(x) = x

plt.figure(figsize=(10, 6))
plt.plot(x_vals, g_vals, label='g(x) = x^2 + x + 1', color='blue')
plt.plot(x_vals, f1_vals, label='f(x) = x^2', color='orange')
plt.plot(x_vals, f2_vals, label='f(x) = x', color='green')
plt.axhline(0, color='black', linewidth=0.5, ls='--')  # Eje horizontal
plt.axvline(0, color='black', linewidth=0.5, ls='--')  # Eje vertical
plt.title('Comparación de funciones')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.ylim(-10, 120)  # Limitar el rango de y para mejor visualización
plt.show()
