"""
Validar precios que debe de incluir el signo de peso, numeros del 0 al 9,
solo 1 punto decimal, si el dato es incorrecto repetira la peticion

48-57 = 0-9
46 = .
36 = $

Seguimos el ejemplo del formato de precios
$123.57
[$,1,2,3,.,5,6]
Tenemos las expresiones \d+ \$? \.?
"""
def validarFormatoDePrecios(cadena) -> True:
    
    isRespuestaAdmitida = False
    coincidenciaSignoPesos = 0
    coincidenciaSignoPunto = 0
    isCoincidenciaSignoPesos = False
    isCoincidenciaSignoPunto = False

    if(ord(cadena[0]) == 36 and (ord(cadena[1]) >= 48 and ord(cadena[1]) <= 57)):
        coincidenciaSignoPesos += 1

        for posicion in range(2,len(cadena)):

            caracterAscii = ord(cadena[posicion])

            if((caracterAscii >= 48 and caracterAscii <= 57) or caracterAscii == 46 or caracterAscii == 36):

                if(caracterAscii == 46):
                    coincidenciaSignoPunto += 1
                elif(caracterAscii == 36):
                    coincidenciaSignoPesos += 1

        if(coincidenciaSignoPesos == 1):
            isCoincidenciaSignoPesos = True
        
        if(coincidenciaSignoPunto >= 0 and coincidenciaSignoPunto <= 1):
            isCoincidenciaSignoPunto = True
 
        if(isCoincidenciaSignoPesos):
            if(isCoincidenciaSignoPunto):
                isRespuestaAdmitida = True
            else:
                print("El valor ingresado contiene mas de un punto (.). Favor de volver a ingresarlo. ")    
        else:
            print("El valor ingresado contiene mas de un signo de pesos ($). Favor de volver a ingresarlo.")
    else:
        print("El valor ingresado no coincide con el comienzo del simbolo de $ pesos o no tiene un digito al comienzo. Favor de volver a ingresar el valor.")                

    return isRespuestaAdmitida

def validarEspaciosPrecio(cadena) -> bool:
    coincidencias = 0
    for caracter in cadena:
        carcaterAscii = ord(caracter)
        if(carcaterAscii == 32):
            coincidencias += 1
    
    if(coincidencias > 0):
        return False
    else:
        return True


def main():
    numero = input("Ingresa el precio de un producto, indicando el signo de $ seguido del valor. \n")
    if(validarEspaciosPrecio(numero)):
        if(validarFormatoDePrecios(numero)):
            print("Formato valido")
        else:
            print("Formato invalido")
            main()
    else:
        print("El valor ingresado es incorrecto ya que este porta espacios. Favor de volver a ingreasarlo.")
        main()

if(__name__ == "__main__"):
    main()