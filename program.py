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
from random import randint

# Fungsi Penjumlahan
def jumlah() :
  a = randint(1,30)
  b = randint(1,30)
  c = a + b
  print(a, ' + ', b, ' = ')
  jawab = input('jawab: ')
  jawab = int(jawab)
  if c == jawab :
     cek = 1
     print(cek)
  else :
     cek = 0
     print(cek)

jumlah()
