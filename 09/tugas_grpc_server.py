import grpc
from concurrent import futures
from sqlmodel import Field, Session, SQLModel, create_engine, select

import tugas_buku_pb2
import tugas_buku_pb2_grpc

class Buku(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kode_rak: str
    judul: str
    harga: float
    apakah_tersedia: bool

engine = create_engine("sqlite:///toko_buku.db")

class BukuServiceServicer(tugas_buku_pb2_grpc.BukuServiceServicer):
    def GetBuku(self, request, context):
        with Session(engine) as session:
            statement = select(Buku).where(Buku.id == request.id)
            results = session.exec(statement)
            buku_result = results.first()
            
            if buku_result is None:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Buku tidak ditemukan")
                return tugas_buku_pb2.BukuResponse()
                
            return tugas_buku_pb2.BukuResponse(
                id=buku_result.id,
                kode_rak=buku_result.kode_rak,
                judul=buku_result.judul,
                harga=buku_result.harga,
                apakah_tersedia=buku_result.apakah_tersedia
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tugas_buku_pb2_grpc.add_BukuServiceServicer_to_server(BukuServiceServicer(), server)
    server.add_insecure_port('[::]:50052')  # Menggunakan port 50052 agar aman
    print("Server gRPC Buku berjalan. Mendengarkan di port 50052...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()