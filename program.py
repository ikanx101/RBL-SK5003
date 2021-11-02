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
    # easy: 1-5
    # medium: 4-9
    # hard: 7 - 15
# ==============================================================

# fungsi untuk clear halaman
def clear():
  for i in range(0,10):
    print("\n\n")


# import fungsi yang dibutuhkan
from random import randint # digunakan untuk melihat waktu
import datetime # untuk melihat waktu
import matplotlib.pyplot as plt # untuk melakukan plot


clear()
print('Halo,\n\nSelamat datang di program generator soal Matematika di Python.\nUntuk memulai, silakan masukkan level kesulitan yang diinginkan:\n')

# fungsi level
# ini masih sederhana ya utk penjumlahan terlebih dahulu
def level():
  print('Level kesulitan soal:\n1. easy\n2. medium\n3. hard\n\n(Masukkan angka level)\n\n')
  lvl = input('level: ')
  lvl = int(lvl)
  if lvl == 1:
    x1 = 1
    x2 = 30
  if lvl == 2:
    x1 = 30
    x2 = 70
  if lvl == 3:
    x1 = 70
    x2 = 200
  out = [x1,x2]
  return(out)

# fungsi untuk menentukan n soal
def n_soal():
  n = input("Banyaknya soal yang mau dikerjakan: ")
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


# =========================================
# tampilannya mulai dari sini

# penentuan level kesulitan
lv = level()

# bikin array untuk rekap
benar = [] # berapa banyak jawaban benar
waktu = [] # waktu yang dibutuhkan
tipe_soal = []

# menentukan seberapa banyak soal yang dikerjakan
print("\n\nPENJUMLAHAN\n")
n_penjumlahan = n_soal()
n_penjumlahan = int(n_penjumlahan) - 1

# menentukan seberapa banyak soal yang dikerjakan
print("\n\nPENGURANGAN\n")
n_pengurangan = n_soal()
n_pengurangan = int(n_pengurangan) - 1

clear()

# mulai iterasi untuk penjumlahan
i = 0
tes = []
while i <= n_penjumlahan :
  tes = jumlah(lv[0],lv[1])
  benar.append(tes[0])
  waktu.append(tes[1])
  tipe_soal.append("jumlah")
  i = i + 1

# mulai iterasi untuk pengurangan
i = 0
while i<=n_pengurangan :
  tes = kurang(lv[0],lv[1])
  benar.append(tes[0])
  waktu.append(tes[1])
  tipe_soal.append("kurang")
  i = i + 1

# output ke user
print("\n\n")
print("Kamu berhasil menjawab: ",sum(benar)," soal dari total ",len(benar)," soal")
print("Waktu yang dibutuhkan: ",round(sum(waktu),4)," detik")

# bikin plot
plt.figure(figsize = (16,9))
plt.plot(waktu,benar,color = "red",linewidth=0.5,linestyle="--",label='delta = 5')
plt.xlabel('time')
plt.ylabel('benar')
plt.legend()
plt.show()
plt.savefig('rekap.png',dpi = 450)
