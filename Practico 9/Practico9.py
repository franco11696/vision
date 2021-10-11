import cv2
import numpy as np
from math import sqrt
from numpy.core.fromnumeric import resize
from Perspectiva import perspectiva

factor = 0.446667858 #Based on the rectified image, the elevator's Door measurement is: h = 2010mm (450px)
#Therefore 2010mm = 450 px --> px = 0.446667858cm 
pts = [[],[]]

def selection (event,x,y,flags,param):
    global drawing, pts, i
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pts[i] = x,y #We create a tuple with mouse's defined coordinates.
        cv2.circle(persp_r, pts[i], 2,  (20,175,80), 2) 
        i = i+1
        if i == 2:
            drawing = False
            cv2.line(backup, (pts[0][0],pts[0][1]), (pts[1][0],pts[1][1]), (20,175,80), 1)
            dist = ". " + str(round((sqrt(((x-pts[0][0])*(factor/100))**2+((y-pts[0][1])*(factor/100))**2)),2)) + " metros"
            cv2.putText(backup, dist, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (20,175,80), 2)

        elif (drawing is True):
            backup[:] = persp_r[:] #Measurement update (avoid measures overlapping) 	

img = cv2.imread('pic.jpeg') #We load the picture.
vector_o = [[210,128], [828,290], [806,850], [284,1268]] #We define the base points to perform the transforamtion.
persp = perspectiva(img, vector_o)
persp_r = cv2.resize(persp, (640,480))
backup = persp_r.copy()
backup_2 = persp_r.copy()
cv2.namedWindow('Measurement')
cv2.setMouseCallback("Measurement", selection)
i=0

run = True
while(run == True):
    cv2.imshow('Measurement',backup)
    k=cv2.waitKey(1)& 0xFF
    if k == ord('r'):
        i = 0
        backup = backup_2.copy()
        persp_r = backup_2.copy()
    if k == ord('q'):
        run = False
    elif k==27:
        break
cv2.destroyAllWindows()