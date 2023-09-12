confirmacion = True

def validarNumeros(cadena) -> bool:
    if(cadena.isdigit()):
        return True
    else:
        return False

def solicitarDatos(variable) -> int:
    confDatos = True
    valorFinal = 0
    while(confDatos):
        valor = input(f"Ingresa el valor de {variable}: \n")
        if(validarNumeros(valor) and int(valor) > 0):
            valorFinal = int(valor)
            confDatos = False
        else:
            input('Valor ingresado invalido, Favor de volver a ingresarlo.')
    
    return valorFinal

while(confirmacion):
    a = solicitarDatos('a')
    b = solicitarDatos('b')
    c = solicitarDatos('c')
    aCuadrado = a ** 2
    bCuadrado = b ** 2
    cCuadrado = c ** 2
    if((aCuadrado + bCuadrado) == cCuadrado):
        print(f'Los cuadrados de los numeros son: a = {aCuadrado} b = {bCuadrado} c = {cCuadrado}')
        print('Por lo tanto la suma de a y b cuadrada obtiene como resultado c cuadrada.')
        print(f'{aCuadrado} + {bCuadrado} = {cCuadrado}')
    else:
        print(f'{aCuadrado} + {bCuadrado} = {cCuadrado}')
        print('Los numeros ingresados no son pitagoricos ya que no cumplen con la fromula de a^2 + b^ = c^2')        

    confir = input('Desea volver a ingresar nuevos valores? s = Si cualquier tecla = No \n')    
    if not confir == 's':
        confirmacion = False