#Guilherme Proença Cravo da Costa - 160068

from cv2 import cv2
import numpy as np
import glob

for g in glob.glob("data/sudoku/*.jpg"): # Criar uma pasta chamada 'sudoku' com as imagens
    img = cv2.imread(g, cv2.IMREAD_COLOR)  
    img = cv2.resize(img,(600,600))  

    _,img2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
    imgray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    
    ret,thresh = cv2.threshold(imgray,127,255,0)

    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]  

    for i in zip(contours,hierarchy):
        contorno_atual = i[0]
        hierarquia_atual = i[1]
        x,y,w,h = cv2.boundingRect(contorno_atual)

        if (hierarquia_atual[3] < 0):            
            if (hierarquia_atual[0] > -1 and x+w < 580 and y+h < 590 and w < 40):
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255), 2)
    
    cv2.imshow('sudoku',img)
    cv2.waitKey(3000)

cv2.destroyAllWindows()