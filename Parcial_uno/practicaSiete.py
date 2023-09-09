'''
Hacer un programa que lea tres numeros validados
y que muestre el mayor, el menor y el de amedias
'''

def validarDato(numero):

    if(numero.isdigit()):
        return True
    else:
        return False

def solicitarDatos():
    numeros = []
    cantidadDatos = 0
    while(cantidadDatos < 3):
        numero = input('Ingresa algun numero: \n')
        if(validarDato(numero)):
            numeroInt = int(numero)
            numeros.append(numeroInt)
            cantidadDatos += 1
        else:
            print('el numero ingresado es incorrecto favor de volver a ingresar. \n')
    return numeros


numeros = solicitarDatos()
numeroMayor = 0
numeroMenor = 0
if(numeros[0] > numeros[1]):
    if(numeros[0] > numeros[2]):
        print('el mayor es: ',numeros[0])
        numeroMayor = numeros[0]
    else:
        print('el mayor es: ',numeros[2])
        numeroMayor = numeros[2]
elif(numeros[1] > numeros[2]):
    print('el numero mayor es :',numeros[1])
    numeroMayor = numeros[1]
else:
    print('el numero mayor es: ',numeros[2])
    numeroMayor = numeros[2]

if(numeros[0] < numeros[1]):
    if(numeros[0] < numeros[2]):
        print('el menor es: ',numeros[0])
        numeroMenor = numeros[0]
    else:
        print('el menor es: ',numeros[2])
        numeroMenor = numeros[2]
elif(numeros[1] < numeros[2]):
    print('el numero menor es :',numeros[1])
    numeroMenor = numeros[1]
else:
    print('el numero menor es: ',numeros[2])
    numeroMenor = numeros[2]

if(numeros[0] > numeroMenor and numeros[0] < numeroMayor):
    print('el numero de a medias es: ', numeros[0])
elif(numeros[1] > numeroMenor and numeros[1] < numeroMayor):
    print('el numero de a medias es: ', numeros[1])
else:
    print('el numero de a medias es: ', numeros[2])