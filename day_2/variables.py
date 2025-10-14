# Day 2: 30 Days of python programming

firstname = 'Mario'
lastname = 'Páez'
fullname = 'Mario Páez'
country = 'España'
city = 'Valladolid'
age = 29
year = 1996
is_married = False
is_true = True
is_light_on = False
variable1, variable2, variable3 = 1, 2, 3

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(variable1))
print(type(variable2))
print(type(variable3))

# Veo que no hace falta el espacio después del string, ya que se añade uno automáticamente. De esta forma escrita, tengo 2
print('Longitud del nombre: ',len(firstname))
print('Longitud del apellido: ',len(lastname))

# Para que tenga sentido hago este if else que creo que no puede hacerse dentro del print
if len(firstname) > len(lastname):
    print('El nombre es',abs(len(firstname)-len(lastname)),'caracter más largo que el apellido')
else:
    print('El nombre es ',abs(len(firstname)-len(lastname)),'caracter más corto que el apellido')

# Todo esto lo pide el ejercicio, a pesar de que no lo imprimimos
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Ahora una parte de pensar del ejercicio, el paso 12.
radio = 30
pi = 3.141592
area_of_circle = pi * (radio ** 2)
print(area_of_circle)
circum_of_circle = 2 * pi * radio
print(circum_of_circle)

# Pedimos un imput al usuario. Nótese que debemos pasarlo a int o python pensará que es un string
radio_usuario = int(input('Introduce el radio para calcular el área de un círculo:'))
area_circulo = pi * (radio_usuario ** 2)
print(area_circulo)

# Finalmente, pedimos nombre, apellido, país y edad del usuario y los guardamos. Aquí sí hace falta el espacio, python no lo introduce

nombre_usuario = input('Introduce tu nombre ')
apellido_usuario = input('Introduce tu apellido ')
pais_usuario = input('Introduce tu país ')
edad_usuario = int(input('Introduce tu edad '))
print(nombre_usuario,apellido_usuario,pais_usuario,edad_usuario)