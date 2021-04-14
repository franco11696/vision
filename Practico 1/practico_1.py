import random
numero = random.randint(0, 100)

intentos = int(input('Ingrese el número de intentos'))
veces = 0

while intentos != 0:
    intentos -= 1
    veces += 1
    x = int(input('Ingrese un numero entre 0 y 100'))

    if x == numero:
        print('Felicitaciones! Le pegaste endespues de ', veces, 'intentos.')
        break
    elif x < numero:
        print('El numero que ingresaste es menor.')
    elif x > numero:
        print('El numero que ingresaste es mayor.')

else:
     print('El número era', numero)