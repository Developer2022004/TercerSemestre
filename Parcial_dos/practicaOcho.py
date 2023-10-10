'''
[a-z_0-9]@[a-z_.][com]
'''
correos = []

def validarDigitos(cadena) -> bool:
    if(cadena.isdigit()):
        return True
    else:
        return False

def validarLetras(cadena) -> bool:
    if(cadena.isalpha()):
        return True
    else:
        return False

def eliminarPilas(lista):
    # FIFO
    if(len(lista) != 0):
        print(f"El elemento {lista[0]} ha sido removido")
        lista.pop(0)
    else:
        print("La accion no se logro completar. Debido a falta de elementos dentro de la lista")

def eliminarColas(lista):
    #LIFO
    if(len(lista) != 0):
        print(f"El elemento {lista[len(lista) - 1]} ha sido removido")
        lista.pop(len(lista) - 1)
    else:
        print("La accion no se logro completar. Debido a falta de elementos dentro de la lista")

def validarCorreo(cadena) -> bool:
    #partira desde nombre@dominio.com   extraera desde la posicion .com
    if(cadena[len(cadena)-4:] == ".com"):
        posicionElementoCadena = cadena.find('@')
        if(posicionElementoCadena != -1):
            nombreCorreo = cadena[0:posicionElementoCadena]
            dominioCorreo = cadena[posicionElementoCadena + 1:len(cadena)-4]
            if(validarLetras(dominioCorreo)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def menu(lista) -> int:
    print("--------Bienvenido al Menu-------")
    print("Selecciona alguna de las siguientes opciones")
    print(" 1 Pilas\n 2 Colas")
    opcion = input("Esperando a que ingreses la opcion: \n")
    if(validarDigitos(opcion)):
        if(int(opcion) == 1):
            eliminarPilas(lista)
            print(f"Elementos restantes en la lista: {lista}")
        elif(int(opcion) == 2):
            eliminarColas(lista)
            print(f"Elementos restantes en la lista: {lista}")
        else:
            print("La opcion ingresada es invalida. Favor de volver a ingresarla.")
            return menu()

        return len(lista)
    else:
        print("El valor igresado no es un digito valido. Favor de volver a ingresarlo.")
        return menu(lista)


def main():
    global correos
    correo = input("Escribe un correo o menu para interactuar con la lista\n")
    if(correo != "menu"):
        if(validarCorreo(correo)):
        #    print(correo)
            correos.append(correo)
            for correo in correos:
                print(correo)
            return main()
        else:
            print("Error al escribir el correo")
            return main()
    else:
        tamanoLista = menu(correos)
        if(tamanoLista == 0):
            print("finalizacion del programa")
        else:
            return main()

    
    


if(__name__ == "__main__"):
    main()