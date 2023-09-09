#arreglos
def validarNumeros(numero):
    if(numero.isdigit()):
        return int(numero)
    else:
        print('No es un numero')
        return 0

b = "" 
a = [0,0,0,0,0,0,0,0,0,0]
posicion = 0
valor = 0
while(b == ""):
    b = input('Escribe un valor: \n')
    valor = validarNumeros(b)
    if (not valor == 0):
        a[posicion] = valor
        posicion += 1
        respuesta = input('Deseas otro')
        if (respuesta == 's'):
            if(posicion > 9):
                print('Arreglo lleno')
                break
            b = ""
    else:
        b = ""

for elemento in a:
    if not elemento == 0:
        print(f'{elemento} \n')
        
"""Investigar en cuaderno a mano que son los arreglos y matrices en python, incluyendo un ejemplo de arreglos y matrices"""
    