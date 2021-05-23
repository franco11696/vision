#A tener en cuenta que se llama a una función del archivo adivina para la ejecución del programa.

from adivina import adivin

print('Este programa sirve para adivinar un número random de 0 a 100')

intentos = int(input('Ingrese el número de intentos: '))
vec = adivin(intentos)



