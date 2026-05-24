import typing
import strawberry
from sqlmodel import Field, Session, SQLModel, create_engine, select

@strawberry.type
class Buku(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  
    kode_rak: str                                           
    judul: str                                              
    harga: float                                            
    apakah_tersedia: bool                                   

engine = create_engine("sqlite:///toko_buku.db")

def get_semua_buku():
    with Session(engine) as session:
        statement = select(Buku)
        results = session.exec(statement).all()
        return results

@strawberry.type
class Query:
    semua_buku: typing.List[Buku] = strawberry.field(resolver=get_semua_buku)

schema = strawberry.Schema(query=Query)