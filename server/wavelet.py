import numpy as np
import pywt
import cv2
def w2d(img,mode="haar",level=1):
    imArray=img
    imArray=np.float32(cv2.cvtColor(imArray,cv2.COLOR_RGB2GRAY))/255
    coeffs=pywt.wavedec2(imArray,mode,level=level)
    coeffs_H=list(coeffs)
    coeffs_H[0]*=0;
    imArray_H=np.uint8(pywt.waverec2(coeffs_H,mode)*255)
    return imArray_H