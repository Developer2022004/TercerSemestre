'''
2.- Hacer un programa que lea una cadena, que la agregue a una lista
 y ademas agregue la lista si la cadena es un palindromo ANA = ANA 
 es decir palabra que se lee al reves completamente igual.
'''
cadenasGuardas = []

def validarString(cadena) -> bool:
    confirmacion = False
    for caracter in cadena:
        caracterAscii = ord(caracter)
        if((caracterAscii >= 97 and caracterAscii <= 122) or (caracterAscii >= 65 and caracterAscii <= 90) or caracterAscii == 32):
            confirmacion = True
        else:
            print("Cadena ingresada invalida, ya que contiene valores fuera de caracteres. Favor de volver a ingresarla")
            confirmacion = False
            break
    
    return confirmacion

def solicitarCadena() -> str:
    cadena = input("Ingresa una cadena la cual sea un palindromo: \n")    
    if(validarString(cadena)):
        return cadena
    else:
        return solicitarCadena()

def main():

    global cadenasGuardas

    cadena = solicitarCadena()
    cadenaRevertida = ""
    for i in range(len(cadena) - 1 , -1 ,-1):
        cadenaRevertida += cadena[i]
    
    if(cadenaRevertida == cadena):
        cadenasGuardas.extend([cadena,"Es palindromo"])
    else:
        cadenasGuardas.extend([cadena,"No es palindromo"])
    
    print(cadenasGuardas)

    confirmacion = input("Deseas volver a ingresar otro valor? S = Si Cualquier tecla = No \n")
    if(confirmacion == "S"):
        return main()
    else:
        print("Finalisacion del programa")
    

if(__name__ == "__main__"):
    main()