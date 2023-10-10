def validarnombre():
    c =0 
    a = input('escribe un nombre con apellidos\n')   
    for i in a:
       if (ord(i))>=97 and ord(i)<=122 or (ord(i))>=65 and ord(i)<=90 or (ord(i))==32:#codigo para validar con ascii
            c += 1
    if c ==len(a):
        return(a)
    else:
        print('Error 404')
        return validarnombre()
    
def validaredad():
    c = 0 
    e = input('escribe la edad de la persona\n')
    for i in e:
        if ord(i)>=48 and ord(i)<=57:
            c += 1
    if c == len(e):
        return int(e)
    else:
        print ('Edad incorrecta')
        return validaredad()
    
    
def listas():
    #print(nombre[0:3])
    ct = 0
    while True:
        nombre = validarnombre()
        edad = validaredad()
        lista.append(nombre)
        lista.append(edad)
        print(lista)
        opcion = input('desea agregar otro nombre? s/n\n')
        if opcion =='s':
            listas()
            ct += 1 
        else:
            break


nombre = 'nombre completo'
lista = []

if __name__=="__main__":
    listas()