'''
Hacer un programa que lea el nombre y precio de un producto,
el programa repetira esta accion hasta que el usuario lo desee,
al finalisar mostrara el total de productos, la sumatoria de los precios, el porcentaje de IVA respecto al total y el total a pagar

'''
cantidadProductos = 0
precioTotal = 0.0
totalPagar = 0.0
iva = 0.0
confirmacion = 0
print('Bienvenido a la calculadora de precios de IBM: \nA continuacion Ingresa los nombres y precios de los productos:\n')

while(confirmacion == 0):

    nombre = input('Ingresa el nombre del producto: \n')
    precioProducto = float(input('Ingresa el precio del producto: \n'))
    precioTotal += precioProducto
    cantidadProductos += 1
    confirmacion = int(input('Deseas agregar mas productos? 0 = SI 1 = NO\n'))

iva = precioTotal * 0.16
totalPagar = precioTotal + iva

print(f'Cantidad de productos ingresados: {cantidadProductos} \n Precio Total: {precioTotal} \n Total Iva: {iva} \n Total a pagar: {totalPagar}')
    