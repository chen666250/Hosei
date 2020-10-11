# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:16:07 2020

@author: chen
"""

import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("xian.jpg")#BGR
print(img.shape)
print("width:%d"%(img.shape[0]))

def show_img(img):
    
    plt.imshow(img)
    plt.axis("off")
    plt.show()


img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

show_img(img)

cv.imwrite("new_xian.jpg",img)
(h,w,c)=img.shape

img[255,255]

x1,y1=(h//2,w//2)

img_nw=img[0:x1,0:y1]

show_img(img_nw)

#图片的平移
def offset(img,num):
    img=img+num
    return img 

show_img(offset(img,40))

















