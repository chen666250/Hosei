# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:34:37 2020

@author: chen
"""

#Histogram Equalization
#sk​=T(rk​)=(L−1)j=0∑k​Pr​(rj​)=MNL−1​j=0∑k​nj​      k=1,2,3...L−1


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#
url="livingroom.png"
img=np.array(Image.open(url))
counts=np.bincount(img.flatten(),minlength=256)
plt.hist(img.flatten(),256,[0,256])
plt.show()
nm=512*512



c_size=counts.size
img1=img.copy()
counts1=counts.cumsum()


T=(counts1-counts1.min())*255/(counts1.max()-counts1.min())
img1=T[img1]

img_p=Image.fromarray(img1)
img_p.show()
