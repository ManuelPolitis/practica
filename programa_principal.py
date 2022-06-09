def suma ():
    numero_uno:int = int(input("Ingrese el primer numero a sumar"))
    numero_dos: int = int(input("Ingrese el segundo numero a sumar"))
    return numero_uno-numero_dos

def resta ():
    numero_uno:int = int(input("Ingrese el primer numero a restar"))
    numero_dos: int = int(input("Ingrese el segundo numero a restar"))
    return numero_uno-numero_dos

def producto():
    numero_uno:int = int(input("Ingrese el primer numero a multiplicar"))
    numero_dos: int = int(input("Ingrese el segundo numero a multiplicar"))
    return numero_uno*numero_dos

def division():
    numero_uno:int = int(input("Ingrese el primer numero a dividir"))
    numero_dos: int = int(input("Ingrese el segundo numero a dividir"))
    return numero_uno/numero_dos



def main():
    operacion_a_realizar:str = input("Inserte si desea realizar una suma, una resta, un producto o una division")

    if operacion_a_realizar == "suma":
        print(suma())
    elif operacion_a_realizar == "resta":
        print(resta())
    elif operacion_a_realizar == "producto":
        print(producto())
    elif operacion_a_realizar == "division":
        print(division())


main()
