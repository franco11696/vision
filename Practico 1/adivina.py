import random

def adivin(inten):

    num = random.randint(0, 100)
    vec = 0

    while inten != 0: #Bucle while para la ejecución del programa.
        inten -= 1 #Disminuimos la flag de intentos con cada pasada.
        vec += 1 #Aumentamos la flag de veces en cada pasada.
        x = int(input('Ingrese un numero entre 0 y 100 --> ')) 

        if x == num: #En este if comparamos el valor ingresado con el número generado random.
            print('Felicitaciones! Le pegaste despues de ', vec, 'intentos.')
            break #Si le pega, sale del while.
        elif x < num:
            print('El numero que ingresaste es menor.')
        elif x > num:
            print('El numero que ingresaste es mayor.')

    else: #Si no le pega en los intentos definidos, sale del bucle while.
        print('El número era', num)


        return


