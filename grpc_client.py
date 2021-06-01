import time
import grpc
import sample_pb2
import sample_pb2_grpc

def run():
    statement=""
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = sample_pb2_grpc.sampleServiceStub(channel)
        while True:
            try:
                start = time.time()
                response = stub.sendData(sample_pb2.Records(data="Hello"))
                statement = response.responseData
                print(str(time.time() - start),statement,sep="  :")
                
                time.sleep(0.001)
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                exit()


def close(channel):
    "Close the channel"
    channel.close()


if __name__ == "__main__":
    run()
