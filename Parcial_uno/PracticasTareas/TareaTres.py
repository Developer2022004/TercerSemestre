'''
Hacer un programa que en un arreglo de String de 7 posiciones se pida, se valide y se pase el arreglo los dias de la semana sin repetir
.isalpha() solo letras

El método casefold () elimina todas las distinciones de casos presentes
en una cadena. Se utiliza para la coincidencia sin casillas, es decir,
ignora los casos cuando se compara

str.capitalize()
Retorna una copia de la cadena con el primer carácter en mayúsculas y el resto en minúsculas.
'''
dias = ["","","","","","",""]
diasSemana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

def validarLetras(cadena) -> bool:
    if(cadena.isalpha()):
        return True
    else:
        return False  

def validarDias(_dia) -> bool:
    global diasSemana
    confirmacion = False
    diaNormalisado = _dia.casefold()

    for diaSemana in diasSemana:
        if(diaNormalisado == diaSemana):
            confirmacion = True
            break
    
    return confirmacion

def comprobarRegistros(_dia,_dias = []) -> bool:
    confirmacion = False
    _dia = _dia.casefold()
    for dia in _dias:
        if(_dia == dia):
            print("Ya existe el dia")
            confirmacion = True
            break

    return confirmacion

print("A continuacion se le pedira ingresar el nombre de los dias de la semana, con el fin de almacenarlos, \nfavor de ingresarlos a continuacion uno por uno: ")

def main() -> None:
    global dias
    for posicion in range(0,len(dias)):
        while(True):

            dia = input("Ingresa un dia de la semana: ")
            if(validarLetras(dia)):
                if(validarDias(dia)):    
                    if(comprobarRegistros(dia,dias)):
                        print(f"Favor de ingresar un dia diferente, ya que {dia} se encuentra registrado.")
                    else:
                        dias[posicion] = dia.casefold()
                        break
                else:
                    print(f"El valor ingresado: ({dia}) no pertenece al nombre de los dias de la semana. \nFavor de ingresar un nombre valido: ")
            else:
                print("Nombre de dia invalido. Favor de ingresar un nombre valido: \n")
    
    for dia in dias:
        print("\n",dia)

    confirmacion = input("Desea volver a iniciar el programa: Si = s No = cualquier tecla \n")
    if(confirmacion == "s"):
        dias = ["","","","","","",""]
        # Recursividad
        main()
    else:
        print("!!ADIOS!!")

main()

