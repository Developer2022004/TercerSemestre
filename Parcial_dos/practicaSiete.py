def ValidarNumeros(n):
   if n.isdigit():
      return True
   else:
      return False
   
def agregarLista():
    n=input('Escribe un numero: ')
    res=ValidarNumeros(n)
    if res==True:
       a.append(n)
    else:
       print('Tiene que ser un numero valido ')        

    
def Eliminar_con_pila():
   res=input('Deseas eliminar un elemento? ')
   if res=='S' or res=='s':
      a.pop(len(a)-1)
      print(a)
      Res=input('Deseas eliminar otro Dato? ')
      if Res == 'S' or Res == 's':
         return Eliminar_con_pila() 
      else:
       print(a)  

def Eliminar_con_cola():
   res=input('Deseas Eliminar un elemento? ')  
   if res=='S' or res=='s':
      a.pop(0)
      print(a)
      Res=input('Desea eliminar otro? ')
      if Res=='S' or Res=='s':
         return Eliminar_con_cola()
      else:
        print(a)

def menu():
    print('1.- Agregar')
    print('2.- Eliminar con pilas')
    print('3.- Eliminar  con colas')
    print('4.- Mostrar listas')
    print('5.-Salir')
    opt = (int(input('Elige una opcion: ')))
    if opt == 1:
      agregarLista()
      return menu()
    if opt==2:
       Eliminar_con_pila()
       return menu()
    if opt==3:
       Eliminar_con_cola()
       return menu()
    if opt ==4:
       print(a)
    if opt != 5:
        return menu()
    

a =[]
if __name__ == "__main__":
 menu()