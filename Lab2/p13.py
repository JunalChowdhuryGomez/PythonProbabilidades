import numpy as np
import matplotlib.pyplot as plt

def calcular_probabilidad_distribucion():
    # Definir la funcion de probabilidad de X
    def probabilidad(x):
        if x == 0:
            return 1 / 20
        elif x == 1:
            return 3 / 20
        elif x == 2:
            return 6 / 20
        elif x == 3:
            return 10 / 20
        else:
            return 0

    # Calcular la funcion de distribucion de X
    distribucion = [probabilidad(x) for x in range(4)]
    funcion_distribucion = np.cumsum(distribucion)

    return distribucion, funcion_distribucion

# Obtener la funcion de probabilidad y la funcion de distribucion
probabilidad_x, funcion_distribucion_x = calcular_probabilidad_distribucion()

# Graficar la funcion de probabilidad
plt.bar(range(4), probabilidad_x, width=0.5, align='center', alpha=0.7)
plt.xlabel("Número de bolas blancas extraídas (X)")
plt.ylabel("Probabilidad")
plt.title("Función de probabilidad de X")
plt.xticks(range(4))
plt.show()

# Graficar la funcion de distribucion
plt.step(range(4), funcion_distribucion_x, where='mid')
plt.xlabel("Número de bolas blancas extraidas (X)")
plt.ylabel("Funcion de distribucion")
plt.title("Funcion de distribución de X")
plt.xticks(range(4))
plt.show()
