import cv2
import numpy as np
from euclidiana import euc
from euclidiana import sc

drawing = False #true if mouse is pressed
mode = True #if True, draw rectangle. Press ’m’ to toggle to curve
ix, iy = -1, -1
run = True
angle = int(input('Ingrese el ángulo: \n'))
tx = int(input('Ingrese la traslación en x: \n'))
ty = int(input('Ingrese la traslación en y: \n'))
s = float(input('Ingrese el factor de escala: \n'))


def draw_circle(event,x,y,flags,param):
    global ix, iy, drawing, mode, fx, fy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            if mode is True:
                cv2.rectangle(img,(ix,iy),(x,y),(100,100,100),-1)
            else:
                cv2.circle(img,(x,y),5,(10,10,10),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if(x < ix):       #I compare the final x cursor's position with it's initialand make it zero if lesser.
             x = 0 
        if(y < iy):
             y = 0
        fx, fy = x, y   #I assign the linal x,y position of the cursor to fx,fy variables.
        if mode is True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)




img = cv2.imread('pic1.png')
backup = img.copy() #Make a copy of the origianl in order to restore and process it.
cv2.namedWindow('Polo')
cv2.setMouseCallback('Polo',draw_circle,img)

while(run == True):
    cv2.imshow('Polo',img)
    k=cv2.waitKey(1)& 0xFF
    if k==ord('m'):
        mode = not mode
    if k == ord('g'):
        img = backup[iy:fy, ix:fx] #I take the coordenates defined by cursor from the backup image and load it into img.
        cv2.imwrite('Recorte.png', img)
    if k == ord('r'):
        img = backup.copy()
    if k == ord('e'):
        img = backup[iy:fy, ix:fx] #I take the coordenates defined by cursor from the backup image and load it into img.
        img = euc(img, angle, tx, ty) #Passing parameters to euc function.
        img = img.copy()
        cv2.imwrite('Recorte-eu.png', img)
    if k == ord('s'):
        img = backup[iy:fy, ix:fx] #I take the coordenates defined by cursor from the backup image and load it into img.
        img = sc(img, angle, tx, ty, s) #Passing parameters to euc function.
        img = img.copy()
        cv2.imwrite('Recorte-sc.png', img)  
    if k == ord('q'):
        run = False
    elif k==27:
        break
cv2.destroyAllWindows()