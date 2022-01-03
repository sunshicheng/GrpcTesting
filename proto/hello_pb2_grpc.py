# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
# 这里需要改成包
import proto.hello_pb2 as hello__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
            '/Greeter/SayHello',
            request_serializer=hello__pb2.SayHelloRequest.SerializeToString,
            response_deserializer=hello__pb2.SayHelloReply.FromString,
        )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SayHello': grpc.unary_unary_rpc_method_handler(
            servicer.SayHello,
            request_deserializer=hello__pb2.SayHelloRequest.FromString,
            response_serializer=hello__pb2.SayHelloReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/SayHello',
                                             hello__pb2.SayHelloRequest.SerializeToString,
                                             hello__pb2.SayHelloReply.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
