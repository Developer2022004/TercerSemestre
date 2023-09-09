'''Hacer un programa que lea un numero y que muestre en pantalla si es par o impar'''

numero = int(input('Escribe un numero: \n'))
a = 8

if numero % 2 == 0:
    if a < 10:
        print('hola')
    print('El numero es: ',numero,' es par')
else:
    print('El numero es: ',numero,'es impar')