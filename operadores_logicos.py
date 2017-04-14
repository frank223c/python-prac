# En Python los operadores logicos son:
# and, or y not

cero = 0
uno = 1
dos = 2

cadena = 'cadena'
texto = "texto"

print(cero and uno)
print(uno and dos)
print(cero and dos)
print(cadena and texto)
print(texto and cadena)
print(dos and cadena)

print('\n')

print(cero or uno)
print(uno or dos)
print(cero or dos)
print(cadena or texto)
print(texto or cadena)
print(dos or cadena)

print('\n')

print(not(cero and uno))
print(not(cero or uno))
print(not(uno and dos))
print(not(uno or dos))
print(not(cero and dos))
print(not(cero or dos))
print(not(cadena and texto))
print(not(cadena or texto))
print(not(texto and cadena))
print(not(texto or cadena))
print(not(dos and cadena))
print(not(dos or cadena))


