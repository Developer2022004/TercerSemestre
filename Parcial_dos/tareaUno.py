"""Hacer un programa que en una lista se almacene nombre,edad y sexo de 5 personas,
 validados los datos, al final mostrara el promedio de las edades, 
 nota las listas debe de representar los nombres en str y edad en int"""

"""__list__.append() agrega valor por valor al final de la lista dinamica
   __list__.extends() translada una serie de valores o vectores al final de la lista dinamica
"""

# def solicitarDatosStr(mensaje) -> str:
#     datoStr = ""
#     confirmacion = True
#     while(confirmacion):
#         dato = input(f"{mensaje} \n")
#         if(validarString(dato)):
#             datoStr = dato
#             confirmacion = False
#         else:
#             print("El valor ingresado no es valido. Favor de volver a ingresarlo.")

#     return datoStr

# def solictarDatosInt(mensaje) -> int:
#     datoInt = 0
#     confirmacion = True
#     while(confirmacion):
#         dato = input(f"{mensaje} \n")
#         if(validarInt(dato)):
#             datoInt = dato
#             confirmacion = False
#         else:
#             print("El valor ingresado no es valido. Favor de volver a ingresarlo.")
    
#     return datoInt
# def solicitarSexo(mensaje) -> str:
#     dato = solicitarDatosStr(mensaje)
#     if not len(dato) == 1:
#         print("El valor ingresado es mayor a un solos caracter. Favor de volver a ingresarlo.")
#         solicitarSexo(mensaje)
#     else:
#         dato = dato.capitalize()
#         if(dato in ["M","F"]):
#             return dato
#         else:
#             print("El valor ingresado no corresponde a ninguno de los generos presentados. Favor de ingresarlo nuevamente.")
#             solicitarSexo(mensaje)

# def solicitarDatosStr(mensaje) -> str:
#     dato = input(f"{mensaje} \n")
#     if(validarString(dato)):
#         return dato
#     else:
#         print("El valor ingresado no es valido. Favor de volver a ingresarlo.")
#         solicitarDatosStr(mensaje)
#         return "Nada"

# def solicitareDatosInt(mensaje) -> int:
#     dato = input(f"{mensaje} \n")
#     if(validarInt(dato)):
#         return int(dato)
#     else:
#         print("El valor ingresado no es valido. Favor de volver a ingresarlo.")
#         solicitareDatosInt(mensaje)

personas = []
personasRegistradas = 0

def validarString(cadena) -> bool:
    if(cadena.isalpha()):
        return True
    else:
        return False

def validarInt(cadena) -> bool:
    if(cadena.isdigit()):
        return True
    else:
        return False

def solicitarDatosStr(mensaje) -> str:
    datoStr = ""
    confirmacion = True
    while(confirmacion):
        dato = input(f"{mensaje} \n")
        if(validarString(dato)):
            datoStr = dato
            confirmacion = False
        else:
            print("El valor ingresado no es valido. Favor de volver a ingresarlo.")
    
    return datoStr

def solicitareDatosInt(mensaje) -> int:
    datoInt = 0
    confirmacion = True
    while(confirmacion):
        dato = input(f"{mensaje} \n")
        if(validarInt(dato)):
            datoInt = int(dato)
            confirmacion = False
        else:
            print("El valor ingresado no es valido. Favor de volver a ingresarlo.")  

    return datoInt

def solicitarSexo(mensaje):
    datoStr = ""
    confirmacion = True
    while(confirmacion):
        dato = solicitarDatosStr(mensaje)
        if not len(dato) == 1:
            print("El valor ingresado contiene caracteres adicionales a los especificados. Favor de volver a ingresarlo.")
        else:
            dato = dato.capitalize()
            if(dato in ["M","F"]):
                datoStr = dato
                confirmacion = False
            else:
                print("El valor ingresado no corresponde a ninguno de los generos presentados. Favor de ingresarlo nuevamente.")
    
    return datoStr

def solicitarEdad(mensaje) -> int:
    datoInt = 0
    confirmacion = True
    while(confirmacion):
        dato = solicitareDatosInt(mensaje)
        if(dato < 110):
            datoInt = dato
            confirmacion = False
        else:
            print("El valor ingresado de la edad es irreal ya que este es mayor a 110 años. Favor de volver a ingresarlo.")
    
    return datoInt
        

def main() -> None:
    global personas,personasRegistradas
    nombre = ""; sexo = ""; edad = 0

    if(personasRegistradas <= 4):

        nombre = solicitarDatosStr(f"Ingresa el nombre de la persona {personasRegistradas + 1}:")
        
        edad = solicitarEdad(f"Ingresa la edad de la persona {personasRegistradas + 1}:")
        
        sexo = solicitarSexo(f"Ingresa el sexo de la persona {personasRegistradas + 1} M = Masculino, F = Femenino:")
    
        personas.extend([nombre,sexo,edad])

        personasRegistradas += 1
        print(personas)
        main()
    else:
        sumaEdadesTotales = 0
        for posicion in range(2,len(personas),3):
            sumaEdadesTotales += personas[posicion]
        
        print(f"Promedio de las edades: {sumaEdadesTotales/personasRegistradas}")

if(__name__ == "__main__"):
    main()