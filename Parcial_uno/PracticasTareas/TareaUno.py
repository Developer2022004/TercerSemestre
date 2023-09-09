'''
Hacer un programa que muestre en pantalla un menú opción 
1: área de un cuadrado opción 
2: área de un círculo opción 
3: área de un triángulo.

Dependiendo de la opción de menú se pedirán los datos correspondientes para calcular el área
* Area del cuadrado es (L)(L)
* Area del circulo es (PI)(r^2)   O   ((PI)(D)^2)/4
* Area del triangulo es ((B)(H))/2

Funcion ord(String) extrae el codigo ascii del caracter, para usar la regresion es necesario aplicar chr(String)
'''
#Libreria para utilizar expresiones regulares
import re as regex
import math as mat

''''
re.compile(ReGex) sirve para inicialisar una expresion regular
re.findall(cadena) sirve para extraer las coincidencias y las separa en un arreglo
len(array|lista|tupla|objeto) devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario.
'''

confirmacion = 0
patron = regex.compile('\d+\.?')

def identificadorDecimales(numero):    
    numero = str(numero)
    coincidencia = len(patron.findall(numero))
    return coincidencia

def areaCuadrado(lado):
    area = lado ** 2
    return area

def areaTriangulo(base,altura):
    area = (base * altura)/2
    return area

def areaCirculo(radio):
    area = mat.pi*(radio**2)
    return area

def operaciones(formula,_numeroUno,_numeroDos = ''):
    #Para verificar si existe un segundo numero esto para calcular el triangulo
    if(_numeroDos):
        primerCoincidencia = identificadorDecimales(_numeroUno)
        segundaCoincidencia = identificadorDecimales(_numeroDos)
        
        #Preguntamos si > 2 es un numero decimal invalido es decir 12.33.33 en cambio si == 2 es un decimal valido 12.89
        #si == 1 es un numero entero
        if(primerCoincidencia > 2 or segundaCoincidencia > 2):
            
            print('LO SENTIMOS. Los numeros Ingresados no son validos')
            
        elif(primerCoincidencia == 2 or segundaCoincidencia == 2):
            
            baseDecimal = float(_numeroUno)
            alturaDecimal = float(_numeroDos)
            print(f'El area es: {formula(baseDecimal,alturaDecimal)} u^2')
            print("Decimal")
        else:
            baseEntera = int(_numeroUno)
            alturaEntera = int(_numeroDos)
            print(f'El area es: {formula(baseEntera,alturaEntera)} u^2')
            print("Entero")
            
    else:
        
        coincidencia = identificadorDecimales(numero)

        if(coincidencia > 2):
            
            print('LO SENTIMOS. El numero ingresado es invalido')
            
        elif(coincidencia == 2):
            
            numeroDecimal = float(numero)
            print(f'El area es: {formula(numeroDecimal)} u^')
            
        else:
            
            numeroEntero = int(numero)
            print(f'El area es: {formula(numeroEntero)} u^2')    
                 
print('!!Bienvenido a la Calculador a de Areas de Figuras Geometricas!! \n A continuacion selecciona una de las siguientes opciones a calcular:')

while(confirmacion != 1):
    print('Opciones: \n 1.- Area de un Cuadrado. \n 2.- Area de un Circulo \n 3.- Area de un Triangulo.')
    opcionString = input('Ingresa el numero de opcion deseada : \n')
    coincidencia = len(patron.findall(opcionString))
    opcionAscii = ord(opcionString) if(coincidencia == 1) else 0
    
    if(opcionAscii > 48 and opcionAscii < 52):
        
        if(opcionAscii == 49):
            #Area del cuadrado
            numero = input('Ingresa la longitud de uno de los lado: \n')
            # print(identificadorDecimales(numero))
            operaciones(areaCuadrado,numero)
        
        if(opcionAscii == 50):
            numero = input('Ingresa el radio del circulo: \n')
            operaciones(areaCirculo,numero)
        
        if(opcionAscii == 51):
            base = input('Ingresa la base del Triangulo: \n')
            altura = input('Ingresa la altura del Triangulo: \n')
            operaciones(areaTriangulo,base,altura)
    else:
        print('Lo sentimos favor de ingresar un numero de opcion valida')
        
    confirmacion = int(input('Desea calcular el area de otra figura? 0 = SI 1 = NO \n'))
    

    