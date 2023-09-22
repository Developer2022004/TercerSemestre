"""ord(chr) transforma los caracteres a ascii chr(int) transoforma el ascii a caracter"""

# def ascii():
#     a = input("Escribe un dato: \n")
#     for i in a:
#         if((ord(i) >= 97 and ord(i) <= 122) or ord(i) == 32):
#             print(ord(i))
#             print(chr(ord(i)))
#         else:
#             print('No es letra o espacio en blanco')

# if(__name__ == "__main__"):
#     ascii()
"""
Hacer un programa que mediante un metodo recursivo valide nombre con apellidos  
NOTA: usar return en la recursividad para evitar la ejecucion del bloque.
No obstante, no se recomienda utilizarlo en funciones que retorne algun valor
"""

def ascii():
    a = input("Escribe un nombre con apellidos: \n")
    contador = 0
    for i in a:
        if((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90) or ord(i) == 32):
            contador += 1
    
    if(contador == len(a)):
        print(a)
    else:
        print("Error... el nombre se escribio mal")
        return ascii()

if(__name__ == "__main__"):
    print(ascii())

