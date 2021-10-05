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

# import fungsi yang dibutuhkan
from random import randint # digunakan untuk melihat waktu
import datetime # untuk melihat waktu

# fungsi level
# ini masih sederhana ya utk penjumlahan terlebih dahulu
def level():
  print('Level kesulitan soal:\n1. easy\n2. medium\n3. hard\n')
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
     print(cek)
  else :
     cek = 0
     print(cek)
  return(cek,total_waktu)

# =========================================
# tampilannya mulai dari sini

# penentuan level kesulitan
lv = level()

# bikin array untuk rekap
benar = [] # berapa banyak jawaban benar
waktu = [] # waktu yang dibutuhkan

# menentukan seberapa banyak soal yang dikerjakan
print("\n\nPENJUMLAHAN\n")
n_penjumlahan = n_soal()
n_penjumlahan = int(n_penjumlahan) - 1

# mulai iterasi untuk penjumlahan
i = 0
tes = []
while i <= n_penjumlahan :
  tes = jumlah(lv[0],lv[1])
  benar.append(tes[0])
  waktu.append(tes[1])
  i = i + 1

# output ke user
print("Kamu berhasil menjawab: ",sum(benar)," soal dari total ",len(benar)," soal")
print("Waktu yang dibutuhkan: ",round(sum(waktu),4)," detik")
