lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = 'cero','uno','dos','tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez'
numbers = 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eigth', 'nine', 'ten'

cadena = []
translate = []

#print(lista, type(lista))
a = len(lista)

#print(tupla, type(tupla))
b = len(tupla)

print(a, type(a))
print(b, type(b))

if a == b:
    print('cadena')
    for i in lista:
        list.append(cadena, str(lista[i]) + '->' + tupla[i])
        list.append(translate, str(lista[i]) + ': ' + tupla[i] + '-' + numbers[i])
else:
    print('saliendo')
print('\n')
print(cadena)
print('\n')
print(lista)
print('\n')
print(tupla)
print('\n')
print(translate)

abecedario = []
vocales = []
consonantes = []
j = 0

for letra in 'ABCDEFGHIJKLMNOPQRcsSTUVWXY':
    #print(j)
    if letra in 'AEIOU':
        print(letra, 'es una vocal')
        list.append(vocales, letra)
        list.append(abecedario, letra)
    else:
        print(letra, 'es una consonante')
        list.append(consonantes, letra)
        list.append(abecedario, letra)
    j += 1

print(abecedario, type(abecedario))
print('\n')
print(vocales, type(vocales))
print('\n')
print(consonantes, type(consonantes))
