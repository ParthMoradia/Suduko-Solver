import cv2
import numpy as np


#def intializePredectionModel():
    #model = load_model('Resources/myModel.h5')
 #   return model
def preProcess(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,1,1,11,2)
    return imgThreshold