import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ======================
# DATOS DEL PROBLEMA
# ======================
q = -1.6e-19   # carga (C)
m = 9.11e-31   # masa (kg)
E = 400        # campo eléctrico (N/C)
vx = 3e6       # velocidad en x (m/s)

# ======================
# CÁLCULO
# ======================
a = q * E / m

# Tiempo: 0 a 3000 ns
t = np.arange(0, 3001, 100) * 1e-9

# Posiciones
x = vx * t
y = 0.5 * a * t**2

# ======================
# (a) FIGURA
# ======================
plt.figure()
plt.scatter(x, y)
plt.plot(x, y)
plt.xlabel("Posición x (m)")
plt.ylabel("Posición y (m)")
plt.title("Figura 1: Movimiento del electrón")
plt.grid()
plt.savefig("figura1.png")
plt.show()

# ======================
# (b) ANIMACIÓN
# ======================
fig, ax = plt.subplots()
ax.set_xlim(0, max(x))
ax.set_ylim(min(y), 0)

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Animación del electrón")

punto, = ax.plot([], [], 'bo')

def actualizar(i):
    punto.set_data(x[i], y[i])
    return punto,

ani = FuncAnimation(fig, actualizar, frames=len(x), interval=200)

# Guardar GIF
ani.save("animacion.gif", writer="pillow")

plt.grid()
plt.show()
