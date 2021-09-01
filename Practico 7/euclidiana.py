import cv2
import numpy as np
import time

def euc(image, angle,tx, ty):      #The function gets it's parameters from Practico5.py.
    angle = np.deg2rad(angle)     #deg2rad used to change degrees (input) to radian.
    (h, w) = image.shape[:2]        #Defines the matrix's size.
    z = np.float32([[np.cos(angle), np.sin(angle), tx],[-np.sin(angle), np.cos(angle), ty],]) #Matrix definition: {(cos(angle) sin(angle) tx}   {-sin(angle) cos(angle) ty)}
    euc = cv2.warpAffine(image, z, (h, w))  #warpAffine transforms an image using a matrix based on the given parameters (image=source, z=transf. matrix, h/w=size of output pic)
    return euc

def sc(image, angle, tx, ty, s):
    angle = np.deg2rad(angle)     #deg2rad used to change degrees (input) to radian.
    (h, w) = image.shape[:2]        #Defines the matrix's size.
    z = np.float32([[s*np.cos(angle), s*np.sin(angle), tx],[s*-np.sin(angle), s*np.cos(angle), ty],]) #Matrix definition: {(cos(angle) sin(angle) tx}   {-sin(angle) cos(angle) ty)}
    sc = cv2.warpAffine(image, z, (h, w))  #warpAffine transforms an image using a matrix based on the given parameters (image=source, z=transf. matrix, h/w=size of output pic)
    return sc

def warp(image, origin, final):
    (h, w) = image.shape[:2]    #Defines the matrix's size.
    z = cv2.getAffineTransform(origin, final) #This function returns an affine transform calculated from three pairs of coodinates using a 2x3 transformation matrix.
    warp= cv2.warpAffine(image, z, (w, h), borderValue=(155, 155, 155)) #warpAffine transforms an image using a matrix based on the given parameters (image=source, z=transf. matrix, h/w=size of output pic). In this case we apply a bordervalue due to the fact we are working with an image's outline.
    return warp 