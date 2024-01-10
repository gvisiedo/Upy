def funcion():
    return ("Hola Mundo")

funcion()

def cuadrado(numero):
    return (numero**2)

cuadrado(5)

def cuadrado2(numero, cuad):
    return (numero**cuad)

cuadrado2(5, 2)

def funcion2(*args):
    for i in args:
        print(i)

funcion2(1,2,5,8,16, "Hola Mundo")

def funcion3(**args):
    for argument in args:
        print(argument, "=>", args[argument])

funcion3(arg1=1, arg2="holamundo")

def devuleveVariosValores():
    return 1,2,"Hola mundo"
devuleveVariosValores()
x,y,w = devuleveVariosValores()

def cuadrado(numero):
    """
    Esta función nos permite elevar al cuadrado un numero
    argumentos:
    numero de tipo numero

    :param numero:
    :return:
    """
    return numero**2

help(cuadrado)

