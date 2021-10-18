#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

MIN_MATCH_COUNT = 10

img1 = cv2.imread('img1.jpeg') # Leemos la imagen 1
img1_bk = img1.copy()
img2 = cv2.imread('img2.jpeg') # Leemos la imagen 2
img2_bk = img2.copy()

dscr = cv2.xfeatures2d.SIFT_create(100) # Inicializamos el detector y el descriptor

kp1 , des1 = dscr.detectAndCompute(img1, None) # Encontramos los puntos clave y los descriptores con SIFT en la imagen 1
kp2 , des2 = dscr.detectAndCompute(img2, None) # Encontramos los puntos clave y los descriptores con SIFT en la imagen 2

cv2.drawKeypoints(img1, kp1, img1_bk) # Se marcan los puntos clave
cv2.drawKeypoints(img2, kp2, img2_bk)
concatenar = np.concatenate((img1_bk, img2_bk), axis=1) # Se concatenan las imágenes horizontalmente
cv2.imwrite('puntos_interes.png', concatenar)
cv2.imshow('Puntos de interes', concatenar)
cv2.waitKey(0)
cv2.destroyAllWindows()

matcher = cv2 . BFMatcher ( cv2 .NORM_L2)

matches = matcher . knnMatch ( des1 , des2 , k =2)

# Guardamos los buenos matches usando el test de razón de Lowe
good = [ ]
for m, n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

if(len(good) > MIN_MATCH_COUNT):
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape (-1, 1, 2)

    H, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0) # Computamos la homografía con RAN-SAC

wimg2 = cv2.warpPerspective(img2, H, img2.shape[:2][::-1]) # Aplicamos la transformación perspectiva H a la imagen 2
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good, None)	
cv2.imwrite('Lowe.jpg',img_matches) # Se guarda la imágen después de aplicar el criterio de Lowe

# Mezclamos ambas imágenes
alpha = 0.5
blend = np.array(wimg2 * alpha + img1 * (1 - alpha), dtype=np.uint8)
cv2.imshow('SIFT', blend)
cv2.imwrite('Resultado_SIFT.jpg',blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
