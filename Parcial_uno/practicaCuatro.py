#Estructuras repetitivas
'''
a = 'hola'
for i in range(1,10): #operador de inicio,final,falsos (numeros finitos a recorrer)
    print(i)

for i in range(1,10,2):
    print(i)

for i in a: #Esto itera sobre cada caracter de la cadenas ya que cabe recordar que los String son tipos de datos compuestos
    print(i)

for i in [7,10]: #Esto [7,10] es una tupla solamente itera sobre los elementos internos
    print(i)

--------------------------------------------------------------------------------------------------
Hacer un programa que lea cinco numeros y que muestre en pantalla cuantos pares y cuantos impares hay

numeroUno = int(input('Ingresa un numero: \n'))
numeroDos = int(input('Ingresa un numero: \n'))
numeroTres = int(input('Ingresa un numero: \n'))
numeroCuatro = int(input('Ingresa un numero: \n'))
numeroCinco = int(input('Ingresa un numero: \n'))
a = 0
b = 0
for i in [numeroUno,numeroDos,numeroTres,numeroCuatro,numeroCinco]:
    if i % 2 == 0:
        a += 1
    else:
        b += 1

print('Los numeros pares son: ', a,'\n','Los numeros impares son: ',b)

------------------------------------------------------------------------
pares = 0
impares = 0
numeros = []

for i in range(0,5):
    numero = int(input('Ingresa un numero: \n'))
    numeros.insert(i,numero)

for i in numeros:
    if i %2 == 0:
        pares += 1
    else:
        impares += 1


pares = 0
impares = 0

for i in range(0,5):
    numero = int(input('Ingresa un numero: \n'))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print('El total de numeros pares son: ',pares,'\n','El total de numeros impares son: ',impares)
    
'''

pares = 0
impares = 0
a = 0

while(a < 5):
    b = int(input('Escribe un numero: \n'))
    if b % 2 == 0:
        pares += 1
    else:
        impares += 1
    a += 1

print('El total de numeros pares son: ',pares,'\n','El total de numeros impares son: ',impares)