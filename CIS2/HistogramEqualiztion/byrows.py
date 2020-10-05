# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 22:14:39 2020

@author: chen
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#
url="livingroom.png"
img=np.array(Image.open(url))

rows=img.shape[0]
img1=img.copy()
for row in range(0,rows):
   r=img1[row,:]
   r_i=(np.bincount(r)/512).cumsum()
   siz=r_i.size
   for pix in range(0,siz):
       img1[row,:][img1[row,:]==pix]=r_i[pix]*229
      
       
       
Image.fromarray(img1).show()