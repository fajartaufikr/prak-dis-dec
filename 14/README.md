# Praktikum Minggu 14 - Smart Contract pada Blockchain

Nama  : FAJAR TAUFIK ROMADHON

NIM   : 235410072

Kelas : IF-1

Mata Kuliah : PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI

## 1. Pengantar 
Solana menggunakan Rust untuk membangun smart contract-nya. Dengan demikian, untuk
membuat smart contract di Solana, peranti pengembangan Rust sudah harus terinstall dengan benar. Catatan ini merupakan sub bagian dari catatan yang ada di https://solana.com/docs/programs/rust dengan beberapa pengembangan. Dengan mempraktekkan catatan ini, diharapkan mahasiswa mempunya gambaran umum tentang smart contract. Jika berminat lebih lanjut, maka diharapkan menguasai bahasa pemrograman Rust.

## 2. Smart Contract di Solana - Native Rust
Buat proyek baru di Rust menggunakan cargo kemudian tambahkan pustaka untuk Solana.

$ cargo new hello_solana –lib

$ cd hello_solana

$ cargo add solana-program
![Clone Repository](image/cr.png)

Edit Cargo.toml
![Clone Repository](image/car.png)

Ganti src/lib.rs
![Clone Repository](image/lib.png)

Build source code smart contract tersebut menggunakan perintah cargo build-sbf. Perintah ini
spesifik untuk Solana. Saat mengerjakan perintah tersebut, cargo akan menginstall semua tools yang diperlukan (jika belum ada):
![Clone Repository](image/build.png)

Hasilnya bisa dilihat pada direktori target/deploy:
![Clone Repository](image/deploy.png)

Buat Keypair Default
![Clone Repository](image/key.png)

Dapatkan SOL dari localnet
![Clone Repository](image/drop.png)

Deploy Program dengan Program ID dari File Keypair
![Clone Repository](image/signa.png)

melihat block
![Clone Repository](image/pro.png)

## 3. Smart Contract di Solana - Menggunakan Anchor Framework
Untuk mengerjakan langkah-langkah berikut, pastikan Solana CLI dan Anchor sudah terinstall,
demikian juga dengan Rust, Node.js, dan Yarn di Node.js 
![Clone Repository](image/ver.png)

Membuat proyek baru:
![Clone Repository](image/anchorinit.png)

Build program yang dihasilkan dari perintah init tersebut:
![Clone Repository](image/anchorbuild.png)

Hasil bisa dilihat di direktori target/deploy:
![Clone Repository](image/tree.png)

Untuk proses pengujian, gunakan perintah anchor test:
![Clone Repository](image/anchortest.png)

Hasil pengujian adalah sebagai berikut:
![Clone Repository](image/hasilanchor.png)

Deploy dengan perintah anchor deploy (atau versi terbaru, disarankan menggunakan anchor
program deploy):
![Clone Repository](image/deployanchorr.png)

Catat program id, kemudian masukkan program id ke Solana Explorer untuk Devnet. Berikut adalah
hasilnya:
![Clone Repository](image/63.png)