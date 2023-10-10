'''
1.- Hacer un programa que lea un dato, si el dato es valido se agregara a una lista, pero solamente su valor ascii. 
Un valor correcto es un numero del 0 al 9 o una letra entre la a y la g, de lo contrario se volvera a pedir el dato.
>NOTA: EL PROGRAMA NO TERMINA HASTA QUE SE ESCRIBA EL VALOR -1
'''

caracteresAscii = []

def validarString(cadena) -> bool:
    confirmacion = False
    for caracter in cadena:
        caracterAscii = ord(caracter)
        if(caracterAscii != 32):
            if((caracterAscii >= 48 and caracterAscii <= 57) or (caracterAscii >= 65 and caracterAscii <= 71) or (caracterAscii >= 97 and caracterAscii <= 103) or caracterAscii == 45):
                confirmacion = True
            else:
                print("El dato ingresado no cumple con las especificaciones. Favor de volver a ingresarlo")
                confirmacion = False
                break
        else:
            print("El dato ingresa contiene espacios. Favor de volver a ingresarlo")
            confirmacion = False
            break
    
    return confirmacion

def solicitarDato() -> str:
    dato = input("Ingresa un dato del 0 - 9, o, de a - z, o digita -1 para salir \n")
    if(validarString(dato)):
        return dato
    else:
        return solicitarDato()

def main():
    global caracteresAscii
    dato = solicitarDato()
    if not dato == "-1":
        for caracterDato in dato:
            caracterAsciiDato = ord(caracterDato)
            caracteresAscii.append(caracterAsciiDato)
        
        print(caracteresAscii)
        return main()
    else:
        print("Fin de la ejecucion")


if(__name__ == "__main__"):
    main();