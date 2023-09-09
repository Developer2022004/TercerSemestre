'''
Hacer un programa que llene obligatoriamente un arreglo de numeros de 5 posiciones previamente validados
y al finalizar debe mostrar cuantos pares y cuantos impares se encuentran en el arreglo
'''

numeros = [0,0,0,0,0]
pares = 0
impares = 0

def validarNumeros(cadena):
    if(cadena.isdigit()):
        return True
    else:
        return False

#nota el ciclo for solo recorre por lo cual no puedes afectar directamente al metodo range()
for i in range(0,5):
    while(True):
        numeroString = input('Ingresa un valor: ')
        if(validarNumeros(numeroString)):
            numeros[i] = int(numeroString)
            break
        else:
            print("No es un numero valido.")

for numero in numeros:
    if(numero %2 == 0):
        pares += 1
    else:
        impares += 1

print(f'Numeros pares: {pares} Numeros impares: {impares}')

