# Praktikum Minggu 3 - Konsistensi dan Replikasi pada Sistem Terdistribusi

Nama  : FAJAR TAUFIK ROMADHON

NIM   : 235410072

Kelas : IF-1

Mata Kuliah : PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI

## Pengantar 
Materi ini membahas tentang cara mengkonfigurasi streaming replication di PostgreSQL 18.
Secara prinsip, sebenarnya sama dengan versi-versi PostgreSQL sebelumnya, hanya saja
letak dari direktori data bukan di /var/lib/postgresql/data lagi tapi berubah di
/var/lib/postgresql/18/docker. Materi ini ditulis berdasarkan materi pada https://medium.com/@eremeykin/how-to-setup-single-primary-postgresql-replication-with-do
cker-compose-98c48f233bbf dengan perubahan signifikan. Kerjakan materi pada bagian ini
dan buat penjelasannya di repo GitHub anda sesuai dengan ketentuan.

## Langkah langkah Praktikum: 

### 1. Prasyarat
Instalasi Docker
 ![Clone Repository](image/dockerver.png)

#### 2. Struktur folder
 ![Clone Repository](image/struktur.png)
    1. 00_init.sql
     ![Clone Repository](image/init.png)
    2. docker-compose.yaml
     ![Clone Repository](image/compose.png)
    3. env.sh
     ![Clone Repository](image/env.png)

### 3. Menjalankan Docker-compose
 ![Clone Repository](image/up.png)

 Cek kedua image apakah berhasil diaktifkan 
 ![Clone Repository](image/ps.png)

### 4. Pengujian
 ![Clone Repository](image/tabel.png)

 ![Clone Repository](image/tabel2.png)

### Uji replikasi data
 ![Clone Repository](image/replikasidata.png)

 ![Clone Repository](image/replikasidata2.png)

 ![Clone Repository](image/sh.png)

 ![Clone Repository](image/down.png)

## Replikasi Master-Master Menggunakan Apache Ignite
### 1. Buat folder baru
 ![Clone Repository](image/ignite.png)

### 2. Buat file docker-compose
 ![Clone Repository](image/dc.png)

 ### 3. Jalankan node
 ![Clone Repository](image/node.png)

### 4. Cek node
 ![Clone Repository](image/ceknode.png)

### 5. Jalankan CLI ignite
 ![Clone Repository](image/ignite2.png)

 ![Clone Repository](image/hasilnode.png)

### Eksekusi perintah sql
Unduh dan eksrtak
 ![Clone Repository](image/sql.png)

 ![Clone Repository](image/schema.png)

 ### Masuk ke mode sql
 ![Clone Repository](image/tabelschema.png)

![Clone Repository](image/sql2.png)

Untuk memeriksa apakah perubahan pada http://localhost:10300 tersebut telah dipropagasi ke node-node lainnya, kita bisa memeriksa dengan melakukan koneksi ke node-node lainnya. Berikut adalah node di http://localhost:10301:

![Clone Repository](image/node2.png)

![Clone Repository](image/monthlysales.png)

Memeriksa http://localhost:10302:

![Clone Repository](image/node3.png)

![Clone Repository](image/dcd.png)