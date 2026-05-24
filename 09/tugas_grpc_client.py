import grpc
import tugas_buku_pb2
import tugas_buku_pb2_grpc

def run_client():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = tugas_buku_pb2_grpc.BukuServiceStub(channel)
        
        print("--- Meminta Data Buku ID 1 ---")
        request_ada = tugas_buku_pb2.BukuRequest(id=1)
        try:
            response = stub.GetBuku(request_ada)
            print(f"Judul Buku : {response.judul}")
            print(f"Kode Rak   : {response.kode_rak}")
            print(f"Harga      : Rp{response.harga}")
            print(f"Tersedia   : {response.apakah_tersedia}")
        except grpc.RpcError as e:
            print(f"Error: {e.code()} - {e.details()}")
            
        print("\n--- Meminta Data Buku ID 99 (Tidak Ada) ---")
        request_tidak_ada = tugas_buku_pb2.BukuRequest(id=99)
        try:
            response = stub.GetBuku(request_tidak_ada)
            print(f"Judul Buku : {response.judul}")
        except grpc.RpcError as e:
            print(f"Error: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run_client()