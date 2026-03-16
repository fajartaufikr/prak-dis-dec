Praktikum Minggu 1 - Pengenalan Git dan GitHub

Nama  : FAJAR TAUFIK ROMADHON

NIM   : 235410072

Kelas : IF-1

Mata Kuliah : PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI

Langkah langkah : 
1. Installasi Git

   Dikarenakan saya sudah menginstall, hanya pengecekan versi Git dengan :

       git --version

3. Konfigurasi Git

         git config --global user.name "fajartaufikr"

         git config --global user.email "fajartaufik545@gmail.com"

5. Membuat Repository di GitHub

    Membuat rapository di GitHub dengan nama "prak-dis-dec", digunakan untuk menyimpan semua laporan praktikum.

6. Clone Repository
 
   Repository yg dibuat kemudian diclone menggunakan perintah :

       git clone https://github.com/fajartaufikr/prak-dis-dec.git

    Setelah itu masuk ke folder repository :

       cd prak-dis-dec

7. Membuat Struktur Folder Praktikum

   Membuat folder untuk setiap minggu praktikum :

        mkdir 01 02 03 04 05 ... dst.

8. Membuat file README.md

    Masuk ke folder minggu pertama :

          cd 01
   
   Membuat file laporan :
   
          echo # Praktikum Minggu 1 > README.md

9. Menambahkan File ke Git

    Menambahkan semua perubahan ke staging area :

         git add .

10. Commit Perubahan

    Menyimpan perubahan dengan pesan commit :

        git commit -m "menambahkan laporan praktikum minggu 1"

11. Upload ke GitHub

    Mengupload file ke repository GitHub :

        git push origin main

Kesimpulan

Pada praktikum minggu pertama ini, saya mempelajari dasar penggunaan Git dan GitHub. Saya berhasil membuat repository, melakukan clone repository, membuat struktur folder praktikum, serta melakukan commit dan push ke GitHub.
