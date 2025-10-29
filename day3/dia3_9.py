# Comprobar si un número es par o impar
print('Vamos a comprobar si un número es par o impar')
numero = int(input('Introduce un número entero '))

paridad = numero % 2

if paridad == 0:
    print('¡El número es par!')
elif paridad == 1:
    print('¡El número es impar!')