print('python tiene',len('python'),'caracteres')
print('dragon tiene',len('dragon'),'caracteres')

# Me piden que haga un statement falso así que

veracidad = True if len('python') != len('dragon') else False
print(veracidad)

on = 'on' in 'python' and 'on' in 'dragon' # Como las dos son ciertas, on vale True
print(on)

jargon = 'jargon' in 'I hope this course is not full of jargon'
print(jargon)

noton = 'on' not in 'python' and 'on' not in 'dragon'
print(noton)

longitud_python = len('python')
float_python = float(longitud_python)
print(type(float_python))
string_python = str(float_python)
print(type(string_python))
