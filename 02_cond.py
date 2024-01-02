print('Introduce tu Edad')
edad = int(input())

if(edad > 18 and edad < 50):
    print('Hola')
else:
    print('Adios')

if(edad > 18 and edad < 50):
    if(edad > 18 and edad <25):
        print('Hola')
    else:
        print('Hola mayores')
elif(edad >40 and edad<75):
    print('Hola muy mayores')
    if (edad > 40 and edad < 60):
        print('Hola')
    else:
        print('Hola mayores')
else:
    print('Adios')

