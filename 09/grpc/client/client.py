import grpc
import service_pb2
import service_pb2_grpc

def run_client():
    # Create a connection (channel) to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (the client)
        # Replace 'SdmService' with the service name defined in your .proto
        stub = service_pb2_grpc.SdmServiceStub(channel)

        # Create a request object (e.g., GetSdmRequest)
        # Pass fields defined in your message (e.g., user_id)
        request = service_pb2.SdmRequest(id=1)
        #request = service_pb2.SdmRequest()

        try:
            response = stub.GetSdm(request)
            print(f"Sdm Name: {response.nama}")
        except grpc.RpcError as e:
            print(f"Error: {e.code()} - {e.details()}")


        request_not_found = service_pb2.SdmRequest(id=10000)
        #request = service_pb2.SdmRequest()

        try:
            response = stub.GetSdm(request_not_found)
            print(f"Sdm Name: {response.nama}")
        except grpc.RpcError as e:
            print(f"Error: {e.code()} - {e.details()}")


if __name__ == '__main__':
    run_client()
