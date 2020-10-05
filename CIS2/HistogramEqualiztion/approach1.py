# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 00:00:41 2020

@author: chen
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
url="livingroom.png"
img=np.array(Image.open(url))

hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf=hist.cumsum()
cdf_normalized=cdf*hist.max()/cdf.max()
plt.plot(cdf_normalized,'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.show()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')


img2=Image.fromarray(cdf[img])
img2.show()