import cv2
import numpy as np


def perspectiva(img, vector_o):
    destiny = np.float32([[0, 0], [img.shape[1], 0],  [img.shape[1],img.shape[0]],[0, img.shape[0]]]) #We define the arrangement of the destiny points in order to perform the transformation.
    origin = np.float32([[vector_o[0]], [vector_o[1]], [vector_o[2]], [vector_o[3]]])
    z = cv2.getPerspectiveTransform(origin, destiny) #This function returns an affine transform #calculated from three pairs of coodinates using a 2x3 transformation matrix.
    perspective = cv2.warpPerspective(img, z, (img.shape[1], img.shape[0])) #warpAffine transforms an image using a #matrix based on the given parameters (image=source, z=transf. matrix, h/w=size of output pic).
    return perspective
    

