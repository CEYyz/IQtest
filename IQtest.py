# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:30:53 2022

@author: edison
"""

import cv2
import numpy as np

def cv2_show(img, name):
    cv2. imshow(name, img)
    cv2. waitKey(0)
    cv2. destroyAllWindows()
#load img
img = cv2.imread('gray1.png', cv2.IMREAD_COLOR)

#AE portion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
h,w, c=img.shape
y,u,v = cv2.split(gray)
avg = np.sum(y)/(h*w)
print('AE =',avg)
cv2_show(img, 'img') 

#AWB
b,g,r = cv2.split(img)
print('AWB_R/G_ALL =', round(np.sum(r)/np.sum(g),2))
print('AWB_B/G_ALL=', round(np.sum(b)/np.sum(g),2))

#ROI
img_LT = img[0:int(h/10), 0:int(w/10), :]
img_LB = img[1-int(h/10):, 0:int(w/10), :]
img_RT = img[0:int(h/10), 1-int(w/10):, :]
img_RB = img[1-int(h/10):, 1-int(w/10):, :]
img_center = img[int(4.5*h/10):int(5.5*h/10), int(4.4*w/10):int(5.5*w/10), :]

h/2+h/10

#color shading
b1,g1,r1 = cv2.split(img_center)
b2,g2,r2 = cv2.split(img_LT)
r_g1 = ((np.sum(r1)/(4.5*5.5*h*w/100))/(np.sum(g1)/(4.5*5.5*h*w/100)))
b_g1 = ((np.sum(b1)/(4.5*5.5*h*w/100))/(np.sum(g1)/(4.5*5.5*h*w/100)))
r_g2 = ((np.sum(r2)/(h*w/100))/(np.sum(g2)/(h*w/100)))
b_g2 = ((np.sum(b2)/(h*w/100))/(np.sum(g2)/(h*w/100)))
print('color_shading')
print('AWB_R/G =', round(r_g1,2), round(r_g2,2))
print('AWB_B/G =', round(b_g1,2), round(b_g2,2))

#lens shading
gray_LT = gray[0:int(h/10), 0:int(w/10), :]
gray_LB = gray[1-int(h/10):, 0:int(w/10), :]
gray_RT = gray[0:int(h/10), 1-int(w/10):, :]
gray_RB = gray[1-int(h/10):, 1-int(w/10):, :]
gray_center = gray[int(4.5*h/10):int(5.5*h/10), int(4.4*w/10):int(5.5*w/10), :]
y1,u1,v1 = cv2.split(gray_center)
y2,u2,v2 = cv2.split(gray_LT)
print((np.sum(y2)/(h*w/100)))
print((np.sum(y1)/(4.5*5.5*h*w/100)))
shading = ((np.sum(y2)/(h*w/100))/(np.sum(y1)/(4.5*5.5*h*w/100)))
print('lens_shading =', round(shading*100,2),'%')
