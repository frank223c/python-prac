# try:
#     try_bloque
# except excepcion1 as variable1:
#     excepcion_bloque1
# ...
# except excepcionN as variableN
#     excepcion_bloqueN

i = input('input a number "int" ')
f = input('input a number "float" ')

try:
    int = int(i)
    print(int, 'is "int"')
except ValueError as err:
    #print(int, 'is not "int"')
    print(err)

try:
    float = float(f)
    print(float, 'is "float"')
except ValueError as err:
    print(err)
