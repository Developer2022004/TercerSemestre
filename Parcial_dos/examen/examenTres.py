'''
3.- Hacer un programa que lea nombre completo con apellidos,
 dia, mes y año de nacimiento, el programa agregara una lista el RFC de la persona
'''

def validarString(cadena) -> bool:
    confirmacion = False

    for caracter in cadena:
        caracterAscii = ord(caracter)
        if((caracterAscii >= 65 and caracterAscii <= 90) or (caracterAscii >= 97 and caracterAscii <= 122) or caracterAscii == 32):
            confirmacion = True
        else:
            confirmacion = False
            print("El valor ingresado es invalido. Favor de volver a ingresarlo")
            break
    
    return confirmacion

def validarNumeros(cadena) -> bool:
    confirmacion = False
    for caracter in cadena:
        caracterAscii = ord(caracter)
        if(caracterAscii >= 48 and caracterAscii <= 57):
            confirmacion = True
        else:
            confirmacion = False
            print("El valor ingresado no es valido. Favor de volver a ingresarlo")
            break
    
    return confirmacion

def solicitarDatoStr(mensaje) -> str:
    dato = input(mensaje)
    if(validarString(dato)):
        return dato
    else:
        return solicitarDatoStr(mensaje)

def solicitarDatosNumeros(mensaje) -> str:
    dato = input(mensaje)
    if(validarNumeros(dato)):
        return dato
    else:
        return solicitarDatosNumeros(mensaje)

def main():
    nombres = solicitarDatoStr("Ingresa tus nombres: \n")
    apellidos = solicitarDatoStr("Ingresa  tus apellidos: \n")
    year = solicitarDatosNumeros("Ingresa tu año de nacimiento: \n")
    mes = solicitarDatosNumeros("Ingresa el mes de nacimiento: \n")
    dia = solicitarDatosNumeros("Ingresa el dia de nacimiento: \n")

    rfc = f'{apellidos[0]}{apellidos[1]{apellidos[1]}{nombres[0]}{}}'

if(__name__ == "__main__"):
    main()