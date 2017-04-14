# el operador "in" es lento en listas y tuplas es lento, mas es veloz en
# y es muy rapido den un diccionario de datos o conjuntos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'e', 'i', 'o', 'u']
tupla= [[1, 'uno'], [2, 3, 4]], [5, 6, 7, 8, 9, 0], ['a', 'e', 'i', 'o', 'u'], ['z'], 'frank'

print(lista, type(lista))

pertenencia = 1 in lista and 'e' in lista

print(pertenencia)
print('z' in lista, 'z' not in lista)

print(tupla, type(tupla))
print(len(tupla))
print([2, 3, 4] in tupla)
print('z' in tupla)
print(['z'] in tupla)
print('frank' in tupla)
print('uno' in tupla)
