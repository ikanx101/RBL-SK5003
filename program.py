"""
=================================
RESEARCH-BASED LEARNING
SK5003 - PEMROGRAMAN DALAM SAINS
=================================

Kelompok RBL 2
20921003 - Winda Wijayasari
20921004 - Mohammad Rizka Fadhli

Program ini bertujuan utk generating random soal
berhitung untuk anak-anak kelas 2-4 SD.
"""

# ==============================================================
# penentuan level berdasarkan angka yang akan digenerate:
  # penjumlahan dan pengurangan: 
    # easy: 1-30
    # medium: 30 - 70
    # hard: 70 - 929
  # perkalian dan pembagian:
    # easy: 1-8
    # medium: 4-12
    # hard: 8-20
# ==============================================================

# fungsi untuk clear halaman
def clear():
  for i in range(0,10):
    print("\n\n")


# import fungsi yang dibutuhkan
from random import randint # digunakan untuk melihat waktu
import datetime # untuk melihat waktu
import matplotlib.pyplot as plt # untuk melakukan plot
import numpy as np


clear()
print('Halo,\n\nSelamat datang di program generator soal Matematika di Python.\nUntuk memulai, silakan masukkan level kesulitan yang diinginkan:\n')

# fungsi level
# ini masih sederhana ya utk penjumlahan terlebih dahulu
def level():
  print('Level kesulitan soal:\n1. easy\n2. medium\n3. hard\n\n(Masukkan angka level)\n\n')
  # digunakan untuk mengecek apakah inputnya berupa integer atau tidak
  marker = True
  while marker:
   try:
    lvl = int(input("level: "))
    if lvl > 3 or lvl < 1:
      marker = True
      print("Masukkan angka sesuai instruksi")
    else: break
   except ValueError:
    print("Format input salah. Masukkan angka sesuai instruksi.\n\n")

  if lvl == 1:
     x1 = 1
     x2 = 30
     x3 = 1
     x4 = 8
  if lvl == 2:
     x1 = 30
     x2 = 70
     x3 = 4
     x4 = 12
  if lvl == 3:
     x1 = 70
     x2 = 200
     x3 = 8
     x4 = 20
  out = [x1,x2,x3,x4]
  return(out)

# fungsi untuk menentukan n soal
def n_soal():
  # memastikan bahwa hanya bleh masuk n berupa integer > 0
  marker = True
  while marker:
   try:
    n = int(input("Banyaknya soal yang mau dikerjakan: "))
    if n < 0:
      marker = True
      print("Masukkan angka bilangan bulat positif.\n\n")
    else: break
   except ValueError:
    print("Masukkan angka sesuai instruksi (bilangan bulat).\n\n")
  return(n)

# fungsi penjumlahan
def jumlah(x1,x2) :
  a = randint(x1,x2)
  b = randint(x1,x2)
  c = a + b
  print(a, ' + ', b, ' = ')
  now = datetime.datetime.now()
  jawab = input('jawab: ')
  end = datetime.datetime.now()
  time_delta = end-now
  total_waktu = time_delta.total_seconds()
  jawab = int(jawab)
  if c == jawab :
     cek = 1
     # print(cek)
  else :
     cek = 0
     # print(cek)
  return(cek,total_waktu)

# fungsi pengurangan
def kurang(x1,x2) :
  a = randint(x1,x2)
  b = randint(x1,x2)
  c = a + b
  print(c, ' - ', a, ' = ')
  now = datetime.datetime.now()
  jawab = input('jawab: ')
  end = datetime.datetime.now()
  time_delta = end-now
  total_waktu = time_delta.total_seconds()
  jawab = int(jawab)
  if b == jawab :
     cek = 1
     # print(cek)
  else :
     cek = 0
     # print(cek)
  return(cek,total_waktu)

# fungsi perkalian
def kali(x3,x4) :
  a = randint(x3,x4)
  b = randint(x3,x4)
  c = a * b
  print(a, ' x ', b, ' = ')
  now = datetime.datetime.now()
  jawab = input('jawab: ')
  end = datetime.datetime.now()
  time_delta = end-now
  total_waktu = time_delta.total_seconds()
  jawab = int(jawab)
  if c == jawab :
     cek = 1
     # print(cek)
  else :
     cek = 0
     # print(cek)
  return(cek,total_waktu)

# fungsi pembagian
def bagi(x3,x4) :
  a = randint(x3,x4)
  b = randint(x3,x4)
  c = a * b
  print(c, ' : ', a, ' = ')
  now = datetime.datetime.now()
  jawab = input('jawab: ')
  end = datetime.datetime.now()
  time_delta = end-now
  total_waktu = time_delta.total_seconds()
  jawab = int(jawab)
  if b == jawab :
     cek = 1
     # print(cek)
  else :
     cek = 0
     # print(cek)
  return(cek,total_waktu)


# =========================================
# tampilannya mulai dari sini

# penentuan level kesulitan
lv = level()

# bikin array untuk rekap
benar = [] # berapa banyak jawaban benar
waktu = [] # waktu yang dibutuhkan
tipe_soal = [] # tipe soal


# menentukan seberapa banyak soal yang dikerjakan
print("\n\nPENJUMLAHAN\n")
n_penjumlahan = n_soal()
n_penjumlahan = int(n_penjumlahan) - 1

# menentukan seberapa banyak soal yang dikerjakan
print("\n\nPENGURANGAN\n")
n_pengurangan = n_soal()
n_pengurangan = int(n_pengurangan) - 1

# menentukan seberapa banyak soal yang dikerjakan
print("\n\nPERKALIAN\n")
n_perkalian = n_soal()
n_perkalian = int(n_perkalian) - 1

# menentukan seberapa banyak soal yang dikerjakan
print("\n\nPEMBAGIAN\n")
n_pembagian = n_soal()
n_pembagian = int(n_pembagian) - 1

clear()

# mulai iterasi untuk penjumlahan
i = 0
tes = []
jumlah_benar = []
while i <= n_penjumlahan :
  tes = jumlah(lv[0],lv[1])
  print("\n")
  benar.append(tes[0])
  waktu.append(tes[1])
  jumlah_benar.append(tes[0])
  tipe_soal.append("Penjumlahan")
  i = i + 1

# mulai iterasi untuk pengurangan
i = 0
kurang_benar = []
while i<=n_pengurangan :
  tes = kurang(lv[0],lv[1])
  print("\n")
  benar.append(tes[0])
  waktu.append(tes[1])
  kurang_benar.append(tes[0])
  tipe_soal.append("Pengurangan")
  i = i + 1

# mulai iterasi untuk perkalian
i = 0
kali_benar = []
while i<=n_perkalian :
  tes = kali(lv[2],lv[3])
  print("\n")
  benar.append(tes[0])
  waktu.append(tes[1])
  kali_benar.append(tes[0])
  tipe_soal.append("Perkalian")
  i = i + 1

# mulai iterasi untuk pembagian
i = 0
bagi_benar = []
while i<=n_pembagian :
  tes = bagi(lv[2],lv[3])
  print("\n")
  benar.append(tes[0])
  waktu.append(tes[1])
  bagi_benar.append(tes[0])
  tipe_soal.append("Pembagian")
  i = i + 1

# output ke user
print("\n\n")
print("Kamu berhasil menjawab: ",sum(benar)," soal dari total ",len(benar)," soal")
print("Waktu yang dibutuhkan: ",round(sum(waktu),4)," detik")

# rekap penjumlahan
print("\n")
jumlah_benar = sum(jumlah_benar)
print("Kamu berhasil menjawab ",jumlah_benar," soal penjumlahan dari ",n_penjumlahan+1," soal")

# rekap pengurangan
print("\n")
kurang_benar = sum(kurang_benar)
print("Kamu berhasil menjawab ",kurang_benar," soal pengurangan dari ",n_pengurangan+1," soal")

# rekap perkalian
print("\n")
kali_benar = sum(kali_benar)
print("Kamu berhasil menjawab ",kali_benar," soal perkalian dari ",n_perkalian+1," soal")

# rekap pembagian
print("\n")
bagi_benar = sum(bagi_benar)
print("Kamu berhasil menjawab ",bagi_benar," soal pembagian dari ",n_pembagian+1," soal")
print("\n\nGrafik skor dan rekap berupa csv sudah tersedia di working directory.\n\n")

# bikin rekap berupa file csv
# memberikan nama file
f = open("rekap_jawaban.csv","w+")
f.write("soal,benar,waktu dibutuhkan,tipe soal\n")
for j in range(0,len(benar)) :
  # print (j,". benar = ",benar[j],"; waktu_dibutuhkan = ",waktu[j],"; tipe soal = ",tipe_soal[j])
  f.write(str(j+1)+","+str(benar[j])+","+str(waktu[j])+","+str(tipe_soal[j])+"\n")
f.close()

# bikin plot
benar_cum = np.cumsum(benar)/len(benar) * 100
benar_cum = np.round(benar_cum,decimals=2)
waktu_cum = np.cumsum(waktu)


plt.figure(figsize = (16,9))
plt.plot(waktu_cum,benar_cum,color = "blue",linewidth=1.5,linestyle="--",label='Skor')
plt.scatter(waktu_cum,benar_cum,color = "green")
plt.xlabel('Waktu Menjawab (dalam detik)')
plt.ylabel('Skor Kumulatif (dalam %)')
plt.title("Cumulative Score Over Time")
#plt.legend()
#plt.show()
plt.savefig('rekap.png',dpi = 450)
