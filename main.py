"""
Auth ： Mr. Sun.
File ：main.py
Time ： 2021/12/25 13:45
Desc : 
"""
from util.grpcTools import GrpcTools
from google.protobuf.pyext import _message
from google.protobuf.reflection import ParseMessage

if __name__ == '__main__':

    client = GrpcTools("localhost:50051")
    # 展示可用services
    print(client.all_services())
    # 展示每个services下面的方法
    print(client.services_methods('Greeter'))

    request_data = {"name": '297999'}
    service = "Greeter"
    unary_unary_method = 'SayHello'
    result = client.request_services(service, unary_unary_method, request_data)
    print(result)


