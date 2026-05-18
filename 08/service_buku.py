from typing import List
from fastapi import Depends, FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Buku(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kode_rak: str
    judul: str
    harga: float
    apakah_tersedia: bool

engine = create_engine("sqlite:///toko_buku.db")

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI(title="RESTful API Toko Buku - Tugas Modul 08")

@app.get("/buku/", response_model=List[Buku])
def read_all_buku(session: Session = Depends(get_session)):
    # SQLModel select statement untuk mengambil seluruh baris data
    statement = select(Buku)
    results = session.exec(statement).all()
    return results