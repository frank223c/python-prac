print('calcular el promedio')

suma = 0
contador = 0
i = 1

numeros = []

while True:
    line =  input('n[' + str(i) + ']: ')
    if line:
        try:
            numero = float(line)
            list.append(numeros, numero)
        except ValueError as err:
            print(err)
            continue
        suma += numero
        contador += 1
    else:
        break
    i += 1
if contador:
    print('\n')
    print('contador:', contador, 'suma:', suma, 'promedio:', suma / contador)

print('cantidad de datos:', contador)
print('\n')
cantidad = len(numeros)
print('\n')
print(numeros, type(numeros))