# Base para la solución del Laboratorio 4

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Variables aleatorias A y B
vaA = stats.norm(0, np.sqrt(22))
vaB = stats.uniform(0, np.sqrt(22))

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio X(t) con N realizaciones
N = 10
M_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso x(t) (A y Z independientes)
for i in range(N):
	A = vaA.rvs()
	B = vaB.rvs()
	m_t = A*np.cos((np.pi/6)*t) + B*np.sin((np.pi/6)*t)
	M_t[i,:] = m_t
	plt.plot(t, m_t)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(M_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado
E = 0*t
plt.plot(t, E, '-.', lw=4)

# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $X(t)$')
plt.xlabel('$t$')
plt.ylabel('$x_i(t)$')
plt.show()

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(M_t[n,:], np.roll(M_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación
RMM = 22*22 * np.cos(np.pi/6*taus)

# Gráficas de correlación para cada realización y la
plt.plot(taus, RMM, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{MM}(\tau)$')
plt.legend()
plt.show()

# Gráficas  media
plt.plot(taus, E, '-.', lw=4, label='Media')
plt.title('Media para las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$E_{X}(\tau)$')
plt.legend()
plt.show()