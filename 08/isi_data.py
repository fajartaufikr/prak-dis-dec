from sqlmodel import Field, Session, SQLModel, create_engine


class Buku(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True) 
    kode_rak: str                                          # Tipe CHAR / VARCHAR
    judul: str                                             # Tipe VARCHAR
    harga: float                                           # Tipe FLOAT
    apakah_tersedia: bool                                  # Tipe BOOLEAN

engine = create_engine("sqlite:///toko_buku.db")

def input_data_uts():
    daftar_buku = [
        Buku(kode_rak="A0001", judul="Laskar Pelangi", harga=95000.0, apakah_tersedia=True),
        Buku(kode_rak="A0002", judul="Bumi Manusia", harga=125000.50, apakah_tersedia=True),
        Buku(kode_rak="B0001", judul="Filosofi Teras", harga=88000.0, apakah_tersedia=False),
        Buku(kode_rak="B0002", judul="Negeri 5 Menara", harga=76000.75, apakah_tersedia=True),
        Buku(kode_rak="C0001", judul="Laut Bercerita", harga=115000.0, apakah_tersedia=False)
    ]
    
    with Session(engine) as session:
        for buku in daftar_buku:
            session.add(buku)
        session.commit()
    print("Sukses! 5 data buku berhasil dimasukkan ke dalam database.")

if __name__ == "__main__":
    input_data_uts()