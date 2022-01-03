"""
Author    : Mr. Sun.
FileName  : stubTools.py
Time      : 2021/12/29 9:06 AM
Desc      :  使用 stub 方式 请求grpc 的工具类
"""
import os
import grpc
import importlib
from google.protobuf.json_format import MessageToDict

project_dir = os.path.dirname(os.path.dirname(__file__))


class GrpcRequest(object):
    def __init__(self, url: str, grpc_file: str, server_stub: str):
        channel = grpc.insecure_channel(url)
        service_stub = importlib.import_module(grpc_file)
        client = eval('service_stub.{}'.format(server_stub))
        self.client = client(channel)

    def request_grpc(self, pb_file: str, method: str, request_data: dict):
        client = self.client
        exec("from {} import {}Request".format(pb_file, method))
        request = "{}Request(**{})".format(method, request_data)
        response = eval("client.{}({})".format(method, request))
        result = MessageToDict(response)
        return result


if __name__ == '__main__':
    client_temp = GrpcRequest("localhost:50051", 'proto.hello_pb2_grpc', 'GreeterStub')
    print(client_temp.request_grpc('proto.hello_pb2', 'SayHello', {"name": 'sunshicheng'}))
