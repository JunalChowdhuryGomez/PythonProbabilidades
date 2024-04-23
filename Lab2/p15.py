def calcular_probabilidad(n):
    # Definir la funcion densidad f(x) 
    def f(x):
        if 0 <= x < 1:
            return x
        elif 1 <= x < 2:
            return k - x / 2
        else:
            return 0

    # Sabiendo que la integral de la funcion densidad de -inf hasta +inf es 1, hallamos k
    k = 2

    # Calcular la probabilidad P(1 - 1/n < X <= 1 + 1/n)
    limite_inferior = 1 - 1 / n
    limite_superior = 1 + 1 / n
    probabilidad = 0
    paso = 0.001  

    # Integración numerica usando la suma de Riemann
    for x in range(int(limite_inferior * 1000), int(limite_superior * 1000)):
        x_val = x / 1000
        probabilidad += f(x_val) * paso

    return probabilidad

# Ejemplo: calcular la probabilidad para n = 10
n = 10
resultado = calcular_probabilidad(n)
print(f"La probabilidad para n = {n} es aproximadamente {resultado:.6f}")
