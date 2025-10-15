# Calcular la pendiente y los puntos de corte de la función y = 2x - 2

def y(x):
    return (2 * x) - 2

def x(y):
    return ((y + 2) / 2)

pendiente = (0 + 2) / (1 - 0)
print('Corte con el eje y en x = ',x(0))
print('Corte con el eje x en y = ',y(0))
print('Pendiente m = ',pendiente)