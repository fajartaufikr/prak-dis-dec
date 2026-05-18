# Praktikum Minggu 8 - Arsitektur Microservices untuk Sistem Terdistribusi

Nama  : FAJAR TAUFIK ROMADHON

NIM   : 235410072

Kelas : IF-1

Mata Kuliah : PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI

## 0. Pengantar 
Microservices adalah salah satu arsitektur yang banyak digunakan pada sistem terdistribusi. Dengan menggunakan arsitektur ini, software terdiri atas frontend yang berisi UI/UX dan merupakan titik interaksi antara pengguna dengan aplikasi. Sisi frontend tersebut kemudian meminta layanan / services dari backend yang berupa service. Untuk saat ini, kebanyakan service tersebut bisa dibuat menggunakan REST API, GraphQL, dan gRPC. Praktik pada mata kuliah ini akan menggunakan REST API dengan pustaka FastAPI dan SQLModel untuk ORM dari Python.

## 1. Persyaratan
1. Cek apakah uv sudah terinstall
![Clone Repository](image/uv.png)

2. Membuat Virtual environment
![Clone Repository](image/venv.png)

3. Instalasi Paket FastAPI dan SQLModel
![Clone Repository](image/sqlinstall.png)

4. Masuk ke SQLlite
![Clone Repository](image/insql.png)

5. Buat database
![Clone Repository](image/dbsql.png)

## 2. Source Code
![Clone Repository](image/services.png)

## 3. Menjalankan Source Code
![Clone Repository](image/unicorn.png)

Untuk memeriksa, akses dari browser atau dari headless tool (curl atau wget):
![Clone Repository](image/browser.png)

![Clone Repository](image/curl.png)

## 4. Tugas
1. Buat satu tabel baru menggunakan SQLite, tabel berbeda dari yang ada pada contoh. Tabel tersebut mempunyai 1 primary key dan setidaknya berisi data dengan tipe INT, CHAR, VARCHAR, BOOLEAN, dan FLOAT.
![Clone Repository](image/tugas1.png)

2. Isikan 5 data menggunakan script Python
![Clone Repository](image/tugas2_script.png)
![Clone Repository](image/tugas2.png)

3. Buat RESTful API endpoint untuk menampilkan semua data yang telah diisikan.
![Clone Repository](image/tugas3_service.png)
![Clone Repository](image/tugas3_server.png)

4. Tampilkan hasil RESTful API endpoint tersebut menggunakan curl.
![Clone Repository](image/tugas4.png)