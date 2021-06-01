from concurrent import futures
import threading
import time
import grpc

# import grpc classes
import sample_pb2
import sample_pb2_grpc

class WPOServicer(sample_pb2_grpc.sampleServiceServicer):

    def __init__(self):
        print("Servicer Running ...")
        self.counter = 0
        self.last_print_time = time.time()

    def __str__(self):
        return self.__class__.__name__

    def sendData(self, request, context):
        response = sample_pb2.Acknowledgement()
        response.responseData = "Welcome"
        return response
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    sample_pb2_grpc.add_sampleServiceServicer_to_server(WPOServicer(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)

serve()