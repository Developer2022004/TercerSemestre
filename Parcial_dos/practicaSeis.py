#cola
def aplicarcola():
 res=input('Deseas eliminar un dato? ')
 if res=='S' or res== 's':
  a.pop(0)
  print(a)
  Res=input('Deseas eliminar otro? ')
  if Res=='S' or Res == 's':
   print(a)
   return aplicarcola()
  else:
   print(a)


def cola():
 a.append(int(input('Escribe un numero: ')))
 res=input('Deseas otro numero? ')
 if res =='S' or res=='s':
  return cola()
 else:
  print(a)
  aplicarcola()
   

a=[]
if __name__ == '__main__':
 cola()