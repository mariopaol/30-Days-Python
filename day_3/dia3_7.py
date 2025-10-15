def y(x):
    return (x ** 2) + (6 * x) + 9

print('Probando valores de x hasta que y = x^2 + 6x + 9 me de 0')
for i in range (10):
    print('Para x =',i,'tenemos y =',y(i))
    print('Para x =',-i,'tenemos y =',y(-i))
