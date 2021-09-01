import cv2
import numpy as np

def euc(image, angle,tx, ty):      #The function gets it's parameters from Practico5.py.
    angle = np.deg2rad(angle)     #deg2rad used to change degrees (input) to radian.
    (h, w) = image.shape[:2]        #Defines the matrix's size.
    z = np.float32([[np.cos(angle), np.sin(angle), tx],[-np.sin(angle), np.cos(angle), ty],]) #Matrix definition: {(cos(angle) sin(angle) tx}   {-sin(angle) cos(angle) ty)}
    euc = cv2.warpAffine(image, z, (h, w))  #warpAffine transforms an image using a matrix based on the given parameters (image=source, z=transf. matrix, h/w=size of output pic)
    return euc

