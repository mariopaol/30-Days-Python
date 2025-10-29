edad = int(input('Introduce tu edad: '))
edad_segundos = edad * 365 * 24 * 60 * 60
print('Has vivido',edad_segundos,'segundos')
restante = (100 * 365 * 24 * 60 * 60) - edad_segundos
print('Si vivieras hasta los 100 años, te quedarían',restante,'segundos de vida')