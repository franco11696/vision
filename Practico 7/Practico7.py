import cv2
import numpy as np
from euclidiana import euc
from euclidiana import sc
from euclidiana import warp

drawing = False #true if mouse is pressed
mode = True #if True, draw rectangle. Press ’m’ to toggle to curve
ix, iy = -1, -1
run = True
angle = int(input('Ingrese el ángulo: \n'))
tx = int(input('Ingrese la traslación en x: \n'))
ty = int(input('Ingrese la traslación en y: \n'))
s = float(input('Ingrese el factor de escala: \n'))


def draw_circle(event,x,y,flags,param):
    global ix, iy, drawing, mode, fx, fy, img, pts
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        pts.append([x, y]) #We create a tuple with mouse's defined coordinates. 
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

def selection(img, i):
    global pts
    pts = []
    cv2.namedWindow('Seleccionar')
    cv2.setMouseCallback('Seleccionar', draw_circle) #We call draw_circle function in order to get the coordinates tuple.
    while True:
        cv2.imshow('Seleccionar', img)
        k = cv2.waitKey(1)
        if len(pts) == i: #3 points must be selected before ending if iteration.
            break
    cv2.destroyAllWindows()
    return np.array(pts, dtype=np.float32)

img = cv2.imread('pic2.jpg')
img1 = cv2.resize(cv2.imread('pic1.png'), img.shape[1::-1]) #Load the 2nd picture while resizing it and inversing the tuple's order and cropping the last position in order to get w x h.
backup = img.copy() #Make a copy of the origianl in order to restore and process it.
backup1 = img1.copy()
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
    if k == ord('a'):
        origin = selection(backup.copy(),3)  #We pass the image and receive the tupple with the point's coordinates.
        final = selection(img1.copy(),3)
        img = warp(img, origin, final) #Here we send the source and destiny points to warp function.
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #We converte the image to B&W in order to apply a thershold to it.
        #In order to layer up two images we need to treshold the upper layer (already in B&W), which returns 0's and 1's values,
        #being 0 the black pixels and 1 the white ones. Thus when adding both pics together we'll add up all but the black pixels.
        ret,mask = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY ) #We apply the threshold, where img2gray is our B&W pic, the two following parameters are the colour limits, and the last part is the threshold type.
        ret,mask_inv = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY_INV ) 
        img2 = cv2.bitwise_and(img1, img1, mask=mask)  #We apply an and between two top layers, including the threshold mask.
        img3 = cv2.bitwise_and(img, img, mask=mask_inv)
        img = cv2.add(img2, img3) #Finally we add up both pictures in order to get our final result.
        cv2.imwrite('T-afin.png', img)  
    if k == ord('q'):
        run = False
    elif k==27:
        break
cv2.destroyAllWindows()