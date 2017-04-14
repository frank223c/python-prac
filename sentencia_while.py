
i = 0
j = 0
sumador = 0

lista = []
lista_2 = []
lista_3 = []
lista_4 = []
lista_5 = []
lista_6 = []

limite = 13

print(type(lista))

# menor a mayor
while i < limite:
    #print(i)
    list.append(lista, i)
    list.append(lista_2, limite - 1 - i)
    #sumador = 
    list.append(lista_3, (lista[i] + lista_2[i]))
    list.append(lista_4, lista_2[i]**lista[i])
    list.append(lista_5, lista[i]**lista_2[i])
    list.append(lista_6,lista_4[i]+lista_5[i])
    i += 1

print(lista)

# de mayor a menor
#while limite > 0:
#    print(limite)
#    list.append(lista_2, limite - 1)
#    limite-=1
     
print(lista_2)
cadena_lista_2 = str(lista_2)
print(cadena_lista_2)
print(type(cadena_lista_2))
print(lista_3)
print(lista_4)
print(lista_5)
#print(lista_6)