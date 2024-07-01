from utlis import *
import cv2
import numpy as np

import sudukoSolver
pathImage='Resources/raw.png'
heightImg = 450
widthImg = 450
img =cv2.imread(pathImage)
img =cv2.resize(img,(widthImg,heightImg))
imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)
imgThreshold = preProcess(img)


imgContours=img.copy()
imgBigContours=img.copy()
contours, hierarchy = cv2.findContours(imgThreshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgContours, contours , -1, (0,255,0),3)


                                                                 
