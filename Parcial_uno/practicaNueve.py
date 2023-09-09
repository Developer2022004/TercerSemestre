'''
Hacer un programa que lea nombre, precio y cantidad de un producto,
Datos previamente validados, donde el usuario determinara cuantos productos se van a introducir,
y al finalizar mostrara el total sin IVA, el IVA del total de productos y el total a pagar.

global variable funciona para variables publicas en todo el codigo. sin embargo cuando se declaran globales no se pueden inicializar

Para mandar a llamar una variable global usamos la siguiente instruccion

global variable
variable = tipo_dato
'''
import re as regex
total = 0.0
patronNumeros = regex.compile('\d+')
patronLetras = regex.compile('\D+')
'''.isnumeric() si tuuviera algun elemento  .isnumeric revisa todos los elementos que coincida solo con numeros si caracteres'''

def validarLetras(cadena):
    confirmacion = True
    coincidencias = len(patronNumeros.findall(cadena))

    if(coincidencias > 0):
        confirmacion = False

    return confirmacion

def validarEnteros(cadena):
    confirmacion = True
    coincidencias = len(patronLetras.findall(cadena))

    if(coincidencias > 0):
        confirmacion = False
    
    return confirmacion

def validarPrecio(cadena):
    confirmacion = False
    try:
        float(cadena)
        return True
    except ValueError:
        return False

def solicitarDatos():
    global total
    nombre = input('Ingresa el nombre del producto: \n')

    while(True):
        if(validarLetras(nombre)):
            break
        else:
            nombre = input('Nombre ingresado invalido, favor de volver a ingresar el nombre: \n')

    _precio = input('Ingresa el precio unitario: \n')
    while(True):
        if(validarPrecio(_precio)):
            precio = float(_precio)
            break
        else:
            _precio = input('El precio ingresado es invalido, favor de ingresarlo nuevamente: \n')
    
    _cantidad = input('Ingresa la cantidad del producto: \n')
    while(True):
        if(validarEnteros(_cantidad)):
            cantidad = int(_cantidad)
            break
        else:
            _cantidad = input('La cantidad ingresada es invalida, favor de ingresarlo nuevamente: \n')
    
    totalProducto = precio * cantidad
    total += totalProducto

def main():
    cantidad = 0
    
    while(True):
        cantidad = input('Ingresa la cantidad de productos a registrar: \n')
        
        if(validarEnteros(cantidad)):
            cantidad = int(cantidad)
            break
        else: 
            print('La cantidad Ingresada no es valida')
    
    for a in range(0,cantidad):
        solicitarDatos()
    
    print(f'TOTAL SIN IVA: {total} El IVA ES: {total * 0.16} EL TOTAL CON IVA ES: {total * 1.16}')

main()

