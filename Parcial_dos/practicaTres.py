"""
Entorno a las listas la declaracion variable[indexInicial:indexFinal] extraera solo los valores que se encuentran entre las posiciones indexInicial e indexFinal
"""
nombre = "nombre completo"
lista = []

"""Funcion para validar nombre con caracteres minusculas"""
def validarNombre(cadena) -> bool:
    confirmacion = True
    for caracter in cadena:
        caracterAscii = ord(caracter)
        if not ((caracterAscii >= 97 and caracterAscii <= 122) or (caracterAscii >= 65 and caracterAscii <= 90) or caracterAscii == 32):
            confirmacion = False
    
    return confirmacion

"""Funcion para validar edad"""
def validarEdad(cadena) -> bool:
    confirmacion = True
    for caracter in cadena:
        caracterAscii = ord(caracter)
        if not (caracterAscii >= 48 and caracterAscii <= 57):
            confirmacion = False
    
    return confirmacion

def solicitarDatos(funcion,mensaje) -> str:
    valorRetornado = ""
    confirmacion = True
    while(confirmacion):
        valor = input(mensaje + ":\n")
        if(funcion(valor)):
            valorRetornado = valor
            confirmacion = False
        else:
            print("El valor ingresado es incorrecto. Favor de volver a ingresarlo.")
    
    return valorRetornado


def listas():
    global lista
    nombre = solicitarDatos(validarNombre,"Ingresa el nombre con apellidos")
    edad = int(solicitarDatos(validarEdad,"Ingresa la edad"))
    lista.append([nombre,edad])

    isConfirmacion = True
    while(isConfirmacion):

        confirmacion = input("Repetir?")
        if(len(confirmacion) == 1 and ord(confirmacion) == 83):
            listas()
        elif(len(confirmacion) == 1 and ord(confirmacion) == 78):
            personas = len(lista)
            sumaEdades = 0
            for persona in lista:
                sumaEdades += persona[1]
            
            print(f"suma edades {sumaEdades} promedio: {sumaEdades/personas}")
            isConfirmacion = False

if (__name__ == "__main__"):
    listas()