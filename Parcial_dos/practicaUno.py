
def main():
    global contador,nombres
    nombre = input('Escribe un nombre \n')
    nombres.append(nombre)
    contador += 1
    if(contador > 3):
        print('EL numero de nombres fueron: ',nombres)
    else:
        main()

contador = 0
nombres = []

# investigar la constante __name__
if __name__ == '__main__':
    main()

"""Hacer un programa que en una lista se almacene nombre,edad y sexo de 5 personas,
 validados los datos, al final mostrara el promedio de las edades, 
 nota las listas debe de representar los nombres en str y edad en int"""
