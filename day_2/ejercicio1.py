entrada = open('input.txt','r')
lista = entrada.readlines()
coordenadas = []
i = 0
for line in lista:
    coordenadas.append(line.split())
    print(coordenadas[i])
    i+=1
    