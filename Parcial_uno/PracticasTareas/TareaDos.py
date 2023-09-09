'''

Hacer un programa que muestre el siguiente menu
1.- Suma
2.- Resta
3.- Multiplicacion
4.- Division con decimales
5.- Division con entero
6.- Potencia
7.- Raiz

'''

#aplicacion de metodos
# la excepcion de ValueError sirve para indicar que el dato ingresado no es compatible con el tipo de dato
# except cumple el papel de catch en java, ademas tambien se encuentra el bloque finally asi como el else
# DATO CURIOSO LOS NUMEROS ENTEROS Y DECIMALES SE PUEDEN INCIALIZAR COMO DECIMALES. OJO CON ESTE DATO MAS NO DECIMALES A ENTEROS  YA QUE LOS REDONDEA
import re as regex

def comprobarDecimal(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False


def menu():
    print('1.- Suma')
    print('2.- Resta')
    print('3.- Multiplicacion')
    print('4.- Division con resultado con decimales')
    print('5.- Division con resultado solo entero')
    print('6.- Potencia')
    print('7.- Raiz')
    print('8.- Salir')

def suma():
    a = int(input('Escribe un numero: \n'))
    b = int(input('Escribe otro numero: \n'))
    print(f'El resultado es: {a+b}')

def resta():
    a = int(input('Ingresa un numero entero: \n'))
    b = int(input('Ingresa un segundo numero entero: \n'))
    print(f'El resultado de la resta es: {a-b}')

def multiplicacion():
    a = int(input('Ingresa un numero entero: \n'))
    b = int(input('Ingresa un segundo numero entero: \n'))
    print(f'El resultado de la resta es: {a*b}')

def raiz():
    a = int(input('Escribe un numero: \n'))
    print(f'El resultado de la raiz cuadrada del numero es: {a ** (1/2)}')

def divisionConDecimal(conDecimal):
    confirmacion = True
    primerNumero = 0.0
    segundoNumero = 0.0

    while(confirmacion):
        a = input('Ingresa un numero: \n')
        b = input('Ingresa un otro numero: \n')

        if(comprobarDecimal(a) and comprobarDecimal(b)):
            confirmacion = False
            primerNumero = float(a)
            segundoNumero = float(b)
        else:
            print('Los numeros ingresados no son correctos. Favor de ingresar numeros validos \n')

    if(conDecimal == True):
        print(f'El resultado de la division con decimales es: {primerNumero / segundoNumero}')

    elif(conDecimal == False):
        print(f'El resultado de la division con enteros es: {int(primerNumero / segundoNumero)}')

def potencia():
    confirmacion = True
    primerNumero = 0.0
    segundoNumero = 0.0

    while(confirmacion):
        a = input('Ingresa el numero que deseas elevar: \n')
        b = input('Ingresa el numero al que deseas elevarlo: \n')

        if(comprobarDecimal(a) and comprobarDecimal(b)):
            confirmacion = False
            primerNumero = float(a)
            segundoNumero = float(b)
        else:
            print('Los numeros ingresados no son validos. Favor de ingresar datos validos \n')
        
    resultado = primerNumero ** segundoNumero
    print(f'El resultado de la exponenciacion es la siguiente: {resultado}')
    
while(True):
    menu()
    op = int(input('Elige una opcion \n'))

    if (op == 1):
        suma()
    if(op == 2):
        resta()
    if(op == 3):
        multiplicacion()
    if(op == 4):
        divisionConDecimal(True)
    if(op == 5):
        divisionConDecimal(False)
    if(op == 6):
        potencia()
    if(op == 7):
        raiz()
    if(op == 8):
        break
    elif(op > 8 or op < 1):
        print('Opcion incorrecta')