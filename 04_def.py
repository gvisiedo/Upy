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