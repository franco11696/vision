import cv2
img = cv2.imread('hoja.png', 0)

i , j = img.shape
# Para resolverlo podemos usar dos for anidados con el fin de recorrer todos los elementos de la imágen como una matriz.

for row in range(i):
    for col in range(j):
        if img[row, col] < 200: #Si el elemento en cuestión es menor al umbral le asigno valor 0.
            img[row, col] = 0


else: #Mostramos este mensaje una vez se recorrió todo el for.
    print('La imágen esta lista')

cv2.imwrite('resultado.png', img) #Creamos el archivo con la imágen nueva.

