#pilas y Colas
def aplicarpila():
 res=input('Deseas eliminar un elemento? ')
 if res=='S' or res == 's':
    a.pop(len(a)-1)#Este metodo elimina el ultimo elemento de la lista
    print(a)
    Res=input('Deseas eliminar otro? ')
    if Res=='S' or Res =='s':
        print(a)
        return aplicarpila()
    else:
        print(a)


def pilas():
 a.append(int(input('Escribe un numero: ')))
 res=input('Deseas otro numero? ')
 if res =='S' or res=='s':
  return pilas()
 else:
  print(a)
  aplicarpila()
   

a=[]
if __name__ == '__main__':
 pilas()
