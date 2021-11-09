# RBL-SK5003

## Repo _Project_ ___Research-Based Learning___ dengan __Python__


Dibuat oleh `20921003` dan `20921004`.

---

## Latar Belakang

Ada ide utk membuat program yang bisa membantu ortu dan anak SD (kelas 2-4) utk latihan berhitung.
 
Inspirasinya datang dari pandemi yang mengharuskan anak2 menjalani pembelajaran jarak jauh. Orang tua akhirnya mengambil peran sebagai guru yang harus mengajarkan berbagai materi pelajaran. Salah satunya matematika atau berhitung. Sementara orang tua juga harus tetap menjalankan pekerjaannya sehari-hari.
 
Sebagai contoh, pada tahun lalu ketika anak saya kelas 3 SD, saya mengalami harus bisa mematangkan materi penjumlahan, pengurangan, perkalian, dan pembagian. Ada kalanya kita memiliki keterbatasan dalam memberikan soal latihan kepada anak.

Atas dasar itu kami mencoba berpikir bahwa proses mengajar mungkin tidak bisa dibuat menjadi "otomatis", namun kita bisa mengotomatiskan proses pemberian latihan soal hingga evaluasi dan penilaian.

Oleh karena itu, kami mengusulkan topik RBL sebagai berikut:

```
Membuat program python yang bisa memberikan soal latihan kepada anak sekaligus memberikan penilaian terhadap jawaban anak tersebut.
```
 
Sebagai gambaran, nanti akan ada 4 tipe soal:
	
1. Penjumlahan
1. Pengurangan
1. Perkalian
1. Pembagian

Akan ada level yang bisa dipilih: _easy_, _medium_, dan _hard_.
 
Kemudian anak bisa menentukan mau berapa soal per tipe soal yang mau dikerjakan. Misal anak tsb mau mengerjakan 4 soal penjumlahan, 3 soal pengurangan, 5 soal perkalian, dan 2 soal pembagian saja.
 
Program Python nya akan men-generate soal random dengan cara men-generate sepasang angka yang kemudian dijadikan soal tergantung tipenya.
 
Setelah anak mengisi soal-soal tersebut, akan ada laporan yang akan keluar. Seperti: total skor, waktu pengerjaan, rata2 waktu pengerjaan per soal, tipe soal yang memiliki skor tertinggi/terendah, dll. 
 
_Report_ ini bisa disajikan dalam bentuk grafik juga.

# _Clone Repo_

Untuk menggunakan `program.py`, silakan _clone repo_ atau _copy file_ `program.py` ke _local_ Anda. Jalankan dengan __Python3__.

---

# _Progress_

## 17 September 2021

Hal yang dikerjakan:

- Pembuatan repo di _github_ sebagai tempat pengerjaan dan jurnal _progress_.
- _Brainstorming_ alur pengerjaan.

Hal yang sedang dipelajari:

1. Cara _generating random integer_ di __Python__.

```
from random import seed
from random import randint
# seed random number generator
seed(1)
# contoh generate integer antara bilangan 0 sampai 10
randint(0, 10) 
```

2. Visualisasi data dengan `matplotlib` 

## 21 September 2021

- Definisi level _easy_, _medium_, dan _hard_.
- _Function_ sederhana untuk penjumlahan.

## 23 September 2021

- Pembuatan proposal sesuai dengan _template_ yang diberikan.

## 27 September 2021
- _Submit_ proposal ke Ms. Teams.

## 28 September 2021
- Proposal presentasi dengan _Xaringan_ __R__.
- Presentasi proposal __RBL__.

Hal yang dipelajari: 

Belajar _function_ untuk mengambil `Sys.time()` dengan _Python_:

```
import datetime
now = datetime.datetime.now()
end = datetime.datetime.now()
time_delta = end-now
total_waktu = time_delta.total_seconds()
```

## 4 Oktober 2021

_Submit_ proposal di _channel Teams_.

## 5 Oktober 2021

`program.py` sudah bisa di-run untuk men-_generate_ soal penjumlahan secara sederhana.

## 12 Oktober 2021

`program.py` sudah bisa di-run secara utuh.

## 19 Oktober 2021

_Software_ dalam bentuk UI sudah dibuat dengan catatan sebagai berikut:

1. Belum ada _output_ berupa grafik.
1. Belum ada _output_ berupa _file_.

## 8 November 2021

_Fixed_ masalah _non positive integer input_ pada `level` soal, `n` soal, dan _non integer input_ pada `jawaban` soal.

## 9 November 2021

Presentasi _RBL_ di kelas.
