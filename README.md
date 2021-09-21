# RBL-SK5003

### Repo Project RBL dengan Python


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
 
Report ini bisa disajikan dalam bentuk grafik juga.

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
