# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sample_pb2 as sample__pb2


class SampleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sendData = channel.unary_unary(
                '/SampleService/sendData',
                request_serializer=sample__pb2.Records.SerializeToString,
                response_deserializer=sample__pb2.Acknowledgement.FromString,
                )


class SampleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def sendData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SampleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sendData': grpc.unary_unary_rpc_method_handler(
                    servicer.sendData,
                    request_deserializer=sample__pb2.Records.FromString,
                    response_serializer=sample__pb2.Acknowledgement.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SampleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SampleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def sendData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SampleService/sendData',
            sample__pb2.Records.SerializeToString,
            sample__pb2.Acknowledgement.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)