numero = 5

contador = 0

while(contador < 5):
    contador +=1
    print(contador)
else:
    print('He terminado')

while(contador < 5):
    contador +=1
    print(contador)
    if(contador == 4):
        contador += 1
else:
    print('He terminado')

lista = [4,5,6]

for element in lista:
    print(element)
else:
    print('He terminado')

cadena = 'Hola Mundo'

for caracter in cadena:
    print(caracter)

cadena = 'Hola Mundo'

for caracter in range(len(cadena)):
    print(cadena[caracter])

cadena = 'Hola Mundo'

for caracter in cadena:
    print(caracter)
    if(caracter==" "):
        break
for caracter in cadena:
   if(caracter==" "):
        continue
   print(caracter)

cadena = 'Hola Mundo'
iterador = iter(cadena)
next(iterador)

cadena = 'Hola Mundo'

for i in range(0,3):
    for element in cadena:
        print(element)