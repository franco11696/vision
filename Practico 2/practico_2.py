#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('hoja.png', 0)

i , j = img.shape
# Para resolverlo podemos usar dos for anidados

for row in range(i):
    for col in range(j):
        if img[row, col] < 200:
            img[row, col] = 0


else:
    print('La imágen esta lista')
# Agregar código aquí
cv2.imwrite('resultado.png', img)

