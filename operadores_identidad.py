# operadores de identidad
# el operador is compara direcciones de memoria, es rapido
# puesto que no compara el contenido del objeto

nombre = 'pedro'
edad = 24

a = ['test', 1]
b = ["test", 1]
c = ['test', 1] 
d = []
e = None

# a = b

nombre_edad = nombre is edad
edad_nombre = edad is nombre

test_a_b = a is b
test_b_a = b is a

test_a_c = a is c
test_c_a = c is a

print(nombre_edad)
print(test_a_b)
print(test_a_c) 

print(edad_nombre)
print(test_b_a)
print(test_c_a)

test_not_none = a is not None
test_none = d is None
test_none_e = e is None

print(test_not_none)
print(test_none)
print(test_none_e)
