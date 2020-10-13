# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 08:32:14 2020

@author: chen
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#
#url="nightview.png"
url="livingroom.png"

#url="nocat.jpg"
img=np.array(Image.open(url).convert('L'))


MN=img.shape[0]*img.shape[1]

ifla=img.flatten()
cot=np.bincount(ifla,minlength=256)
nk=cot/(MN)#512*512

sk=np.zeros(256)
for k in range(0,256):
    sk[k]=255*nk[0:k].sum()
    print("k is ",k,"sk  is",sk[k] )

img1=img.copy()
for pix in range(0,256):
    img1[img==pix]=sk[pix]
    
#img1=sk[img]
#Image.fromarray(img1).show()
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.title("origin")
plt.imshow(Image.open(url),'gray')

plt.subplot(1,2,2)
plt.title("processed")
plt.imshow(img1,'gray')

plt.show()

