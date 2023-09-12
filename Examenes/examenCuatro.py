def validarNumeros(cadena) -> bool:
    if(cadena.isdigit()):
        return True
    else:
        return False

def pedirDatos() -> int:
    confirmacion = True
    valorEntero = 0

    while(confirmacion):
        valor = input('Ingresa un numero entero: \n')
        if(validarNumeros(valor)):
            if(int(valor) > 0):
                valorEntero = int(valor)
                confirmacion = False
            else:
                print('Valor ingresado invalido, ya que este es negativo, favor de ingresar un numero positivo.')
        else:
            print('El valor ingresado es incorrecto. Favor de ingresa el dato nuevamente.')
    
    return valorEntero

def main() -> None:
    print('A continuacion ingresa la cantidad de veces que deseas introducir numeros: \n')
    cantidadNumeros = pedirDatos()

    for vuelta in range(0,cantidadNumeros):
        numero = 0
        confirmacion = True

        while(confirmacion):
            print(f'Ingresa el valor del numero vacio en la posicion {vuelta + 1}: \n')
            _numero = pedirDatos()
            if(_numero > 4):
                numero = _numero
                confirmacion = False
            else:
                print('Numero ingresado invalido. Favor de ingresar numeros mayores a 4.')       

        if(numero % 4 == 0):
            print('YES')
        else:
            print('NO')

conf = True
while(conf):
    main()
    res = input('¿Deseas ingresar ingresar mas cantidades? s = Si cualquier tecla = No \n')
    if not res == 's':
        conf = False
        