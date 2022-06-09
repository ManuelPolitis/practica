def suma ():
    numero_uno:int = int(input("Ingrese el primer numero a sumar"))
    numero_dos: int = int(input("Ingrese el segundo numero a sumar"))
    return numero_uno-numero_dos

def resta ():
    numero_uno:int = int(input("Ingrese el primer numero a restar"))
    numero_dos: int = int(input("Ingrese el segundo numero a restar"))
    return numero_uno-numero_dos

def main():
    operacion_a_realizar:str = input("Inserte si desea realizar una suma o una resta")

    if operacion_a_realizar == "suma":
        suma()
    if operacion_a_realizar == "resta":
        resta()


main()
