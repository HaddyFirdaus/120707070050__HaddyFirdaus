import matplotlib.pyplot as plt
import cv2
#%matplotlib inline

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
from skimage.util import invert

import numpy as np

#percobaan 1 crop image

img = cv2.imread('Mikasa.jpg')
img2 = cv2.imread('levi.jpg')

MikasaCropped = img.copy()
MikasaCropped = MikasaCropped[0:256,64:320]

leviCropped = img2.copy()
leviCropped = leviCropped[64:256,128:320]

print('Mikasa Ori Shape : ',img.shape)
print('Mikasa Crop Shape : ',img.shape)

print('levi Ori Shape : ',img2.shape)
print('levi Crop Shape : ',img2.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title("Citra Input 1")

ax[1].imshow(img2, cmap='gray')
ax[1].set_title('Citra Input 2')

ax[2].imshow(MikasaCropped)
ax[2].set_title("Citra Output 1")

ax[3].imshow(leviCropped, cmap='gray')
ax[3].set_title('Citra Output 2')
plt.show()


#Percobaan 2 - Citra Negative
inv = invert(MikasaCropped)
print('Shape Input : ', MikasaCropped.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(MikasaCropped)
ax[0].set_title("Citra Input")

ax[1].hist(MikasaCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')
plt.show()

copyCamera = leviCropped.copy().astype(float)

shape = copyCamera.shape 
output1 = np.empty(shape)

for baris in range(0, shape[0]-1):
    for kolom in range(0, shape[1]-1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] /192
        
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(leviCropped, cmap='gray')
ax[0].set_title("Citra Input")
ax[1].hist(leviCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')
ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')
ax[3].hist(output1.ravel(), bins=192)
ax[3].set_title('Histogram Input')
print(output1.shape)
plt.show()