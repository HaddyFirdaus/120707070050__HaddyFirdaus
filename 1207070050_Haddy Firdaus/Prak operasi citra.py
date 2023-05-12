import matplotlib.pyplot as plt#mengimpor library matplotlib
import cv2#mengimport library open cv2
#%matplotlib inline

from skimage import data# Mengimpor modul data dari pustaka Scikit-image. Modul data menyediakan beberapa dataset gambar bawaan yang dapat digunakan untuk keperluan pengujian atau latihan.
from skimage.io import imread#Mengimpor modul imread dari pustaka Scikit-image. Modul imread digunakan untuk membaca file gambar dari sistem file atau URL.
from skimage.color import rgb2gray#Mengimpor modul rgb2gray dari pustaka Scikit-image. Modul rgb2gray digunakan untuk mengkonversi gambar berwarna menjadi grayscale.
from skimage.util import invert#Mengimpor modul invert dari pustaka Scikit-image. Modul invert digunakan untuk membalikkan nilai piksel pada gambar.

import numpy as np#Mengimpor pustaka NumPy sebagai alias np. NumPy adalah pustaka Python untuk komputasi ilmiah, terutama operasi pada array multidimensi. 

#percobaan 1 crop image

img = cv2.imread('Mikasa.jpg')#membaca gambar dengan nama file 'Mikasa.jpg' menggunakan pustaka OpenCV dan menyimpannya ke dalam variabel img.
img2 = cv2.imread('Levi.jpg')# membaca gambar dengan nama file 'Levi.jpg' menggunakan pustaka OpenCV dan menyimpannya ke dalam variabel img2.

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)# mengkonversi gambar yang disimpan dalam variabel img dari format BGR menjadi RGB menggunakan pustaka OpenCV dan menyimpannya ke dalam variabel RGB_img.
RGB_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)#mengkonversi gambar yang disimpan dalam variabel img2 dari format BGR menjadi RGB menggunakan pustaka OpenCV dan menyimpannya ke dalam variabel RGB_img2.


MikasaCropped = RGB_img.copy()#menyalin gambar dari variabel RGB_img ke variabel MikasaCropped.
MikasaCropped = MikasaCropped[0:256,64:320]#memotong bagian tertentu dari gambar yang disimpan dalam variabel MikasaCropped.

LeviCropped = RGB_img2.copy()#menyalin gambar dari variabel RGB_img2 ke variabel LeviCropped.
LeviCropped = LeviCropped[64:256,128:320]#memotong bagian tertentu dari gambar yang disimpan dalam variabel LeviCropped

print('Mikasa Ori Shape : ',RGB_img.shape)#menampilkan dimensi gambar yang disimpan dalam variabel RGB_img.
print('Mikasa Crop Shape : ',MikasaCropped.shape)# menampilkan dimensi gambar yang disimpan dalam variabel MikasaCropped.

print('Levi Ori Shape : ',RGB_img2.shape)#menampilkan dimensi gambar yang disimpan dalam variabel RGB_img2.
print('Levi Crop Shape : ',LeviCropped.shape)#menampilkan dimensi gambar yang disimpan dalam variabel LeviCropped.

fig, axes = plt.subplots(2, 2, figsize=(12, 12))#membuat 2x2 subplot untuk menampilkan 2 gambar input dan 2 gambar hasil crop.
ax = axes.ravel()#meratakan array 2 dimensi menjadi array 1 dimensi.

ax[0].imshow(RGB_img)#menampilkan gambar asli dari variabel RGB_img pada subplot pertama.
ax[0].set_title("Citra Input 1")#memberikan judul pada subplot pertama.

ax[1].imshow(RGB_img2, cmap='gray')#menampilkan gambar asli dari variabel RGB_img2 dengan colormap 'gray' pada subplot kedua.
ax[1].set_title('Citra Input 2')# memberikan judul pada subplot kedua.

ax[2].imshow(MikasaCropped)# menampilkan hasil crop pada gambar mikasa
ax[2].set_title("Citra Output 1")# memberikan judul pada subplot ketiga.

ax[3].imshow(LeviCropped, cmap='gray')# menampilkan hasil crop pada gambar levi dengan colormap 'gray'
ax[3].set_title('Citra Output 2')# memberikan judul pada subplot keempat.
plt.show()# Menampilkan 4 figure subplots


#Percobaan 2 - Citra Negative
inv = invert(MikasaCropped)#membuat citra yang dihasilkan dari proses inversi (negatif) dari citra MikasaCropped.
print('Shape Input : ', MikasaCropped.shape)#mencetak dimensi citra input.
print('Shape Output : ',inv.shape)#encetak dimensi citra output setelah dilakukan inversi.

fig, axes = plt.subplots(2, 2, figsize=(12, 12))#membuat sebuah figure dengan empat sumbu gambar (axes) dengan ukuran 12x12.
ax = axes.ravel()# memasukkan keempat sumbu gambar ke dalam satu dimensi array.

ax[0].imshow(MikasaCropped)#menampilkan citra input pada sumbu gambar pertama.
ax[0].set_title("Citra Input")#memberi judul pada sumbu gambar pertama.

ax[1].hist(MikasaCropped.ravel(), bins=256)#menampilkan histogram citra input pada sumbu gambar kedua.
ax[1].set_title('Histogram Input')# memberi judul pada sumbu gambar kedua.

ax[2].imshow(inv)#menampilkan citra hasil inversi pada sumbu gambar ketiga.
ax[2].set_title('Citra Output (Inverted Image)')#memberi judul pada sumbu gambar ketiga.

ax[3].hist(inv.ravel(), bins=256)#menampilkan histogram citra hasil inversi pada sumbu gambar keempat.
ax[3].set_title('Histogram Output')# memberi judul pada sumbu gambar keempat.
plt.show()#menampilkan figure yang telah dibuat.

copyCamera = LeviCropped.copy().astype(float)# Mendefinisikan variabel copyCamera sebagai copy dari gambar LeviCropped dalam format float.

shape = copyCamera.shape# Mendefinisikan variabel shape sebagai dimensi dari copyCamera.
output1 = np.empty(shape)#Mendefinisikan variabel output1 sebagai array kosong dengan dimensi shape.

for baris in range(0, shape[0]-1):#Melakukan looping pada setiap baris dalam range dimensi baris copyCamera.
    for kolom in range(0, shape[1]-1):# Melakukan looping pada setiap kolom dalam range dimensi kolom copyCamera.
        a1 = baris# Mendefinisikan variabel a1 adalah baris.
        b1 = kolom# Mendefinisikan variabel b1 adalah kolom.
        output1[a1, b1] = copyCamera[baris, kolom] /192##Menghitung nilai pixel baru pada output1 dengan membagi nilai pixel pada copyCamera pada setiap baris dan kolom dengan 192.
        
fig, axes = plt.subplots(2, 2, figsize=(12, 12))# Mendefinisikan 4 plot untuk menampilkan gambar input, histogram input, gambar output, dan histogram output.
ax = axes.ravel()#Menyusun plot dalam bentuk array 1 dimensi.

ax[0].imshow(LeviCropped, cmap='gray')#Menampilkan citra input pada ax[0].
ax[0].set_title("Citra Input")# Memberikan judul pada plot ax[0].
ax[1].hist(LeviCropped.ravel(), bins=256)#Menampilkan histogram citra input pada ax[1].
ax[1].set_title('Histogram Input')# Memberikan judul pada plot ax[1].
ax[2].imshow(output1, cmap='gray')# Menampilkan citra output pada ax[2].
ax[2].set_title('Citra Output (Brightnes)')#Memberikan judul pada plot ax[2].
ax[3].hist(output1.ravel(), bins=192)#Menampilkan histogram citra output pada ax[3].
ax[3].set_title('Histogram Input')#Memberikan judul pada plot ax[3].
print(output1.shape)#Menampilkan dimensi dari output1.
plt.show()#Menampilkan plot.