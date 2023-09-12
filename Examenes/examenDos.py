nombres = []
contadorIniciales = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
iniciales = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def validarLetras(cadena) -> bool:
    if(cadena.isalpha()):
        return True
    else:
        return False

def validarNumeros(cadena) -> bool:
    if(cadena.isdigit()):
        return True
    else:
        return False

def posicionIniciales(cadena) -> int:
    global iniciales
    posicionEncontrada = 0
    posicionIndex = 0

    for inicial in iniciales:
        if(cadena[0] == inicial):
            posicionEncontrada = posicionIndex
            break
        else:
            posicionIndex += 1

    return posicionEncontrada
            
def contador(posicionIndex) -> None:
    global contadorIniciales
    contador = contadorIniciales[posicionIndex]
    contador += 1
    contadorIniciales[posicionIndex] = contador

def main():
    global nombres 
    global iniciales

    for vuelta in range(0,2):
        #Recoleccion de nombres
        confNombre = True
        while(confNombre):
            nombre = input(f'Ingresa el nombe de la persona {vuelta + 1}: \n')
            if(validarLetras(nombre)):
                nombre = nombre.capitalize()
                nombres.append(nombre)
                confNombre = False
            else:
                print('Nombre invalido, favor de volver a ingresarlo.')

        #Recoleccion de edades
        confEdad = True
        while(confEdad):
            edad = input('Ingresa la edad de la persona: ')
            if(validarNumeros(edad) and int(edad) > 0):
                confEdad = False
            else:
                print('Edad ingresada invalida, favor de volver a ingresarla.')
    
        #Recoleccion de sexo
        confSexo = True
        while(confSexo):
            sexo = input('Ingresa el sexo de la persona, (M = Masculino o F = Femenino): ')
            if(validarLetras(sexo) and (sexo == 'M' or sexo == 'F')):
                confSexo = False
            else:
                print('Sexo ingresado invalido, favor de volver a ingresarlo.')

    for nombre in nombres:
        posicionIndex = posicionIniciales(nombre)
        contador(posicionIndex)

    posicion = 0
    print('El total de las iniciales de los nombres se muestra a continuacion:')

    for inicial in iniciales:
        print(f'{inicial}: {contadorIniciales[posicion]}')
        posicion += 1


while(True):
    contadorIniciales = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    main()
    confirmacion = input('Desea volver a ejecutar el programa? s = Si cualquier tecla = No ')
    if not confirmacion == 's':
        break  