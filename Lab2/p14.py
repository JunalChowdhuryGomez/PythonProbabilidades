import numpy as np

def calcular_media_y_varianza(n):
    # funcion de densidad f(x) 
    def f(x):
        return np.where((0 <= x) & (x < 1), k * (1 - x**2), 0)

    # Sabiendo que la integral de la funcion densidad de -inf hasta +inf es 1, hallamos k
    k = 3 / 4

    # Calcular la media y la varianza de Y = X^n
    x_vals = np.linspace(0, 1, num=1000)
    media_y = np.trapz(x_vals**n * f(x_vals), x_vals)
    varianza_y = np.trapz((x_vals**n - media_y)**2 * f(x_vals), x_vals)

    return media_y, varianza_y

for n in range(1,10):
    media, varianza = calcular_media_y_varianza(n)
    print(f"Para n = {n}, la media de Y = X^n es aproximadamente {media:.6f}")
    print(f"Para n = {n}, la varianza de Y = X^n es aproximadamente {varianza:.6f}")
    print()
