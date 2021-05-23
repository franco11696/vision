import sys
import cv2

#if(len(sys.argv)>1):
#    filename = sys.argv[1]
#else:
#    print('Pass a file name as first argument')
#    sys.exit(0)

cap = cv2.VideoCapture('filename.mp4') #Cargamos el video a procesar.

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#A.¿Cómo obtener el frame rate o fps usando las OpenCV? Usarlo para no tener que harcodear el delay del waitKey.
#B. ¿Cómo obtener el ancho y alto de las imágenes capturadas usando las OpenCV? Usarlo para no tener que harcodear el frameSize del video generado.

fps = cap.get(cv2.CAP_PROP_FPS)  #Usamos este comando para obtener los FPS adecuados.
framesize = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) #Usamos este comando para obtener el tamaño exacto a capturar.
delay = int(1000/fps) #Dividimos un segundo por la cantidad de FPS para evitar definirlo nosotros. Lo defino como int porque sino tengo problemas en el cv2.waitKey (linea 27).
#------------------------------------------------------------------------------------------------------------------------------------------------------
#framesize = (640,480)
out = cv2.VideoWriter('output.avi',fourcc,fps,framesize,isColor = False)


while(cap.isOpened()):
    ret,frame = cap.read()
    if ret is True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.imshow('Imagegray',gray)
        if cv2.waitKey(delay)&0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()