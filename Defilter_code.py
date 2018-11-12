#python2
#libraries required are opencv, numpy
import cv2 as cv
import numpy as np
#import matplotlib.pyplot as py
import math


def PSNR(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )      #MSE
    if mse == 0:
        return -1 #psnr is infinite and both the image are same
    return 20*math.log10(255.0/mse**0.5)      #formula for PSNR



def Reverse(J,N): 
    X=J
    for i in range(N):
        #J_=f(X)
        J_=cv.GaussianBlur(X,(15,15),5)
        residue=np.subtract(J,J_)
        X=np.add(np.multiply(X,0.6),residue)
        #X=np.uint8(X)
    return X

im=cv.imread('butterfly.jpg')
J=cv.GaussianBlur(im,(15,15),5)
#for i in range(15):
#    X=Reverse(J,i)
#    cv.imwrite('Reverse'+str(i)+'.jpg',np.uint8(X))
X=Reverse(J,100)
cv.imwrite('Reverse.jpg',np.uint8(X))

cv.imwrite('Blur.jpg',np.uint8(J))
print PSNR(im,X)
print PSNR(im,J)
