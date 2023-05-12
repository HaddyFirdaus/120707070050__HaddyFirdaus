import numpy as np#mengimport dari library numpy
import cv2#mengimport library open cv
import imageio#mengimport library imageio
import matplotlib.pyplot as plt#mengimport library matplotlib

img = cv2.imread('Mikasa.jpg')#membaca gambar dari cv2

#define reso dan tipe gambar
img_height = img.shape[0]# mengambil dimensi pertama dari objek NumPy array img, yang merepresentasikan tinggi dari gambar.
img_width = img.shape[1]#mengambil dimensi kedua dari objek NumPy array img, yang merepresentasikan lebar dari gambar.
img_channel = img.shape[2]#mengambil dimensi ketiga dari objek NumPy array img, yang merepresentasikan jumlah channel dari gambar.
img_type = img.dtype#mengambil tipe data dari objek NumPy array img. Tipe data ini dapat berupa uint8 (unsigned integer 8-bit), float32 (floating point 32-bit), atau tipe data lainnya

#Percobaan pertama kita buat brightness untuk gambar gray scale
#membuat variable img_brightness untuk menampung

img_brightness = np.zeros(img.shape, dtype=np.uint8)#membuat sebuah array NumPy dengan ukuran yang sama dengan gambar img dan tipe data uint8

#membuat fungsi penambahan brightness dengan nilai yang menjadi parameter
def brighter(nilai) :# mendefinisikan sebuah fungsi bernama brighter dengan satu parameter nilai.
    for y in range(0, img_height):#melakukan looping sebanyak tinggi gambar
        for x in range(0, img_width):#melakukan looping sebanyak lebar gambar
            red = img[y][x][0]#mengekstrak nilai warna merah pada koordinat piksel tertentu pada gambar img.
            green = img[y][x][1]#mengekstrak nilai warna hijau pada koordinat piksel tertentu pada gambar img.
            blue = img[y][x][2]##mengekstrak nilai warna biru pada koordinat piksel tertentu pada gambar img.
            gray = (int(red)+int(green)+int(blue))/3# menghitung nilai rata-rata dari tiga komponen warna untuk menghasilkan warna abu-abu pada koordinat piksel tersebut.
            gray += nilai#menambahkan nilai brightness pada nilai rata-rata warna abu-abu tersebut.
            if gray > 255:#memastikan nilai kecerahan pada koordinat piksel tidak melebihi batas atas.
                gray = 255
            if gray < 0:#memastikan nilai kecerahan pada koordinat piksel tidak melebihi bawah.
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)#menyimpan nilai kecerahan yang telah dimodifikasi ke dalam array img_brightness.

fig, axes = plt.subplots(2, 1, figsize=(5, 5))#membuat objek gambar dengan dua subplots.
ax = axes.ravel()#digunakan untuk mengubah array axes yang berbentuk multidimensi menjadi array satu dimensi.
brighter(-100)#memanggil fungsi brighter untuk mengatur kecerahan gambar. Parameter nilai yang digunakan adalah -100.
ax[0].imshow(img_brightness)#ini menampilkan gambar hasil modifikasi kecerahan pada subplot pertama.
ax[0].set_title("Brighness -100")#Baris kode ini memberikan judul pada masing-masing subplot.
brighter(50)#memanggil fungsi brighter untuk mengatur kecerahan gambar. Parameter nilai yang digunakan adalah 50.
ax[1].imshow(img_brightness)#ini menampilkan gambar hasil modifikasi kecerahan pada subplot kedua.
ax[1].set_title("Brighness 50")#Baris kode ini memberikan judul pada masing-masing subplot.
fig.tight_layout()#menampilkan objek gambar yang telah dibuat.
plt.show()#menampilkan objek gambar yang telah dibuat.

#brightness RGB
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)#membuat sebuah array NumPy dengan ukuran yang sama dengan gambar img dan tipe data uint8

#Fungsi untuk brightness RGB dengan nilai parameter
def rgbbrighter(nilai):# mendefinisikan sebuah fungsi bernama brighter dengan satu parameter nilai.
    for y in range(0, img_height):#melakukan looping sebanyak tinggi gambar
        for x in range(0, img_width):#melakukan looping sebanyak lebar gambar
            red = img[y][x][0]#Mendapatkan nilai channel merah (red) pada pixel (x, y) di gambar img.
            red += nilai#Menambahkan nilai brightness (nilai) ke nilai channel merah (red) pixel (x, y).
            if red > 255:#nilai channel merah (red) pixel (x, y) melebihi 255, maka nilai tersebut akan diset menjadi 255.
                red = 255
            if red < 0:#nilai channel merah (red) pixel (x, y) kurang dari 0, maka nilai tersebut akan diset menjadi 0.
                red = 0
            green = img[y][x][1]#Mendapatkan nilai channel hijau (green) pada pixel (x, y) di gambar img.
            green += nilai#Menambahkan nilai brightness (nilai) ke nilai channel hijau (hijau) pixel (x, y).
            if green > 255:#nilai channel hijau (green) pixel (x, y) melebihi 255, maka nilai tersebut akan diset menjadi 255
                green = 255
            if green < 0:#nilai channel hijau pixel (x, y) kurang dari 0, maka nilai tersebut akan diset menjadi 0.
                green = 0
            blue = img[y][x][2]#Mendapatkan nilai channel biru (blue) pada pixel (x, y) di gambar img.
            blue += nilai##Menambahkan nilai brightness (nilai) ke nilai channel biru (blue) pixel (x, y).
            if blue > 255:#nilai channel blue pixel (x, y) melebihi 255, maka nilai tersebut akan diset menjadi 25
                blue = 255
            if blue < 0:#nilai channel blue pixel (x, y) kurang dari 0, maka nilai tersebut akan diset menjadi 0.
                blue = 0
            img_brightness[y][x] = (red, green, blue)#Menyimpan nilai channel merah (red), hijau (green), dan biru (blue) pada pixel (x, y) yang telah diubah ke dalam gambar img_brightness.
fig, axes = plt.subplots(2, 1, figsize=(5, 5))# Membuat sebuah objek figure dan 2 subplot pada grid 2x1.
ax = axes.ravel()#Meratakan array 2 dimensi axes menjadi 1 dimensi.
rgbbrighter(-100)#Memanggil fungsi rgbbrighter dengan parameter nilai -100 untuk mengubah gambar img_brightness
ax[0].imshow(img_brightness)#Menampilkan gambar hasil perubahan brightness pada subplot pertama.
ax[0].set_title("Brighness -100")# Memberikan judul pada subplot pertama.
rgbbrighter(50)#Memanggil fungsi rgbbrighter dengan parameter nilai 50 untuk mengubah gambar img_brightness
ax[1].imshow(img_brightness)#Menampilkan gambar hasil perubahan brightness pada subplot kedua.
ax[1].set_title("Brighness 50")# Memberikan judul pada subplot pertama.
fig.tight_layout()#menampilkan objek gambar yang telah dibuat.
plt.show()##menampilkan objek gambar yang telah dibuat.

img_contrass = np.zeros(img.shape, dtype=np.uint8)#endefinisikan sebuah array NumPy dengan nama img_contrass dan menginisialisasinya dengan nilai nol dengan tipe data unsigned integer 8-bit (uint8).

def contrass(nilai):#Mendefinisikan sebuah fungsi bernama contrass yang menerima parameter nilai.
    for y in range(0, img_height):#Memulai loop for untuk melakukan iterasi pada setiap baris citra.
        for x in range(0,img_width):#Memulai loop for di dalam loop sebelumnya untuk melakukan iterasi pada setiap kolom citra.
            red= img[y][x][0]#Mendapatkan nilai pixel warna merah pada posisi (x,y) citra.
            green= img[y][x][1]#Mendapatkan nilai pixel warna hijau pada posisi (x,y) citra.
            blue= img[y][x][2]#Mendapatkan nilai pixel warna biru pada posisi (x,y) citra.
            gray= (int(red)+int(green)+int(blue))/3#Menghitung nilai keabuan dari nilai pixel pada posisi (x,y) dengan menjumlahkan nilai pixel warna merah, hijau, dan biru pada posisi tersebut, lalu membaginya dengan 3.
            gray+= nilai#Menambahkan nilai kontras yang diterima sebagai parameter ke nilai keabuan pixel pada posisi (x,y).
            img_contrass[y][x]= (gray, gray, gray)#Menetapkan nilai pixel pada posisi (x,y) pada array img_contrass dengan nilai keabuan pixel yang baru (yang sudah diubah pada baris sebelumnya) ke dalam ketiga komponen warna merah, hijau, dan biru.

            img_contrass[y][x] = (red, green, blue)#Menetapkan kembali nilai pixel pada posisi (x,y) pada array img_contrass dengan nilai pixel warna asli (tanpa perubahan kontras) ke dalam ketiga komponen warna merah, hijau, dan biru.
fig, axes = plt.subplots(2, 1, figsize=(5, 5))#Membuat sebuah figure dan dua buah subplot untuk menampilkan citra asli dan citra hasil perubahan kontras.
ax = axes.ravel()#Menggabungkan kedua subplot ke dalam sebuah array 1 dimensi.
contrass(2)#Memanggil fungsi contrass dengan parameter 2 untuk melakukan perubahan kontras pada citra.
ax[0].imshow(img_contrass)#Menampilkan citra hasil perubahan kontras pada subplot pertama.
ax[0].set_title("Contras 2")#Memberikan judul pada subplot pertama.
contrass(3)# Memanggil fungsi contrass dengan parameter 3 untuk melakukan perubahan kontras pada citra.
ax[1].imshow(img_contrass)#Menampilkan citra hasil perubahan kontras pada subplot kedua.
ax[1].set_title("Contras 3")#Memberikan judul pada subplot kedua.
fig.tight_layout()#
plt.show()##menampilkan objek gambar yang telah dibuat.

#Membuat variabel img_contrass untuk menampung hasil
img_autocontrass = np.zeros(img.shape, dtype=np.uint8)#Membuat sebuah variabel numpy array dengan nama img_autocontrass yang akan digunakan untuk menyimpan hasil gambar yang sudah ditambahkan kontras.
#Melakukan penambahan contrass secara otomatis
def autocontrass():#Mendefinisikan sebuah fungsi dengan nama autocontrass() yang berfungsi untuk melakukan penambahan kontras secara otomatis pada gambar.
    xmax = 300#Menginisialisasi variabel xmax dengan nilai 300
    xmin = 0#variabel xmin dengan nilai 0,
    d = 0#variabel d dengan nilai 0.
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):#mendefinisikan loop for untuk mengakses setiap piksel di gambar dengan ukuran img_height
        for x in range(0, img_width):#mendefinisikan loop for untuk mengakses setiap piksel di gambar dengan ukuran img_width.
            red = img[y][x][0]#Mengekstrak nilai red dari piksel di baris y dan kolom x.
            green = img[y][x][1]#Mengekstrak nilai green dari piksel di baris y dan kolom x.
            blue = img[y][x][2]# Mengekstrak nilai blue dari piksel di baris y dan kolom x.
            gray = (int(red) + int(green) + int(blue)) / 3# Menghitung nilai rata-rata dari ketiga komponen warna (red, green, dan blue) untuk menghasilkan nilai kecerahan atau intensitas warna (grayscale) pada piksel.
            if gray < xmax:#perbandingan antara nilai kecerahan (grayscale) pada setiap piksel dengan nilai piksel terbesar pada gambar
                xmax = gray
            if gray > xmin:#perbandingan antara nilai kecerahan (grayscale) pada setiap piksel dengan nilai piksel terkecil dan terbesar pada gambar
                xmin = gray
    d = xmin-xmax#Menetapkan nilai piksel yang telah disesuaikan ke dalam variabel img_autocontrass.
    for y in range(0, img_height):#mendefinisikan loop for untuk mengakses setiap piksel di gambar dengan ukuran img_height
        for x in range(0, img_width):#mendefinisikan loop for untuk mengakses setiap piksel di gambar dengan ukuran img_width
            red = img[y][x][0]#Mengekstrak nilai red dari piksel di baris y dan kolom x.
            green = img[y][x][1]#Mengekstrak nilai green dari piksel di baris y dan kolom x.
            blue = img[y][x][2]#Mengekstrak nilai blue dari piksel di baris y dan kolom x.
            gray = (int(red) + int(green) + int(blue)) / 3#Menetapkan nilai piksel yang telah disesuaikan ke dalam variabel img_autocontrass.
            gray = int(float(255/d) * (gray-xmax))#menyesuaikan nilai kecerahan pada piksel dengan mengurangi nilai xmax dan mengalikan dengan skala kontras yang baru dihitung (255/d). Kemudian, nilai kecerahan diubah ke dalam bilangan bulat.
            img_autocontrass[y][x] = (gray, gray, gray)#Menetapkan nilai piksel yang telah disesuaikan ke dalam variabel img_autocontrass.
autocontrass()#Panggilan fungsi untuk menyesuaikan kontras gambar.
plt.imshow(img_autocontrass)#Menampilkan gambar yang telah disesuaikan kontrasnya dengan menggunakan Matplotlib.
plt.title("Contrass Autolevel")# Membuat judul gambar
plt.show()##menampilkan objek gambar yang telah dibuat.













