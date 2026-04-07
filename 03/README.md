# Praktikum Minggu 3 - Sinkronisasi pada Sistem Terdistribusi

Nama  : FAJAR TAUFIK ROMADHON

NIM   : 235410072

Kelas : IF-1

Mata Kuliah : PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI

## Pengantar 
Ada 2 protokol yang biasanya digunakan untuk sinkronisasi waktu: NTP (Network Time
Protocol) dan PTP (Precision Time Protocol).

## Langkah langkah Praktikum: 

### I. Sinkronisasi waktu

1. Install NetTime pada link berikut https://www.timesynctool.com/
2. Penjelasan

### II. Vector Clock
Vector clock digunakan untuk pengurutan event dalam suatu sistem terdistribusi. Berikutadalah contoh source code untuk vector clock (ada pada source code: vclocks.py). Source code diambil dari banyak sumber di Internet.


Tugas:
1. Jalankan program tersebut, amati keluarannya. Buat penjelasan dari keluaran tersebut: bandingkan dengan algoritma tersebut jika vector clocks dilaksanakan secara manual.
2. Buat modul Python untuk class VectorClock tersebut dan buatlah contoh cara menggunakan modul tersebut.

### III. Problem Tanpa Sinkronisasi
Pada sistem terdistribusi, ketiadaan sinkronisasi bisa menghasilkan 2 masalah besar yaitu data race / race conditions dan deadlock. Pada program yang menggunakan model asynchronous maupun thread, pola pikir sekuensial tidak bisa digunakan karena penyelesaian satu task dengan task lainnya biasanya tidak bisa diprediksi. Berikut adalah
contoh program multithreaded di Python (multithreaded-example.py).

Tugas:
1. Jalankan program tersebut sampai anda mendapatkan keluaran yang berbeda.
2. Capture keluaran program tersebut dan jelaskan mengapa bisa berbeda.