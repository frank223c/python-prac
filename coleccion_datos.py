# las tuplas son inmutables

nombre = 'franklin',
tupla = [1,2,'tres'],[],['franklin']
lista = [1,2,'tres']
cadena = 'rudy franklin'

print(nombre, type(nombre))
print(len(nombre))
print(tupla, type(tupla))
print(len(tupla))
print(lista, type(lista))
print(len(lista))
print(cadena, type(cadena))
print(len(cadena))

lista.append('rudy')
print(lista)

#forma correcta de escribir
list.append(lista, 'condori')
print(lista)
print(tupla[2])
print(tupla[10])
