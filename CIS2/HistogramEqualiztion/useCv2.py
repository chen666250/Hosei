# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:26:49 2020

@author: chen
"""
import cv2
img = cv2.imread("livingroom.png")  

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("src", gray)

dst = cv2.equalizeHist(gray)
cv2.imshow("dst", dst)

cv2.waitKey(0)