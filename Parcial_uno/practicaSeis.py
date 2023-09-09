def leerDatos():
    a = input('Escribe un valor')
    return a

def validarDatos(a):
    if(a.isdigit()):
        return 'son numeros \n'
    else:
        return 'no son numeros \n'
    
a = leerDatos()
print(validarDatos(a))