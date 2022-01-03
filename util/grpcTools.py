"""
Author    : Mr. Sun.
FileName  : send_requests.py
Time      : 2021/12/27 10:51 AM
Desc      :  处理反射获取服务的工具类
"""
import json
import importlib
from grpc_requests import Client, StubClient


# 使用此方法需要服务开启反射，否者执行不了
class GrpcTools(object):
    def __init__(self, url):
        self.client = Client.get_by_endpoint(url)

    # 获取所有的服务
    def all_services(self):
        return self.client.service_names

    # 获取一个服务下的所有方法
    def services_methods(self, services: str):
        """
        :param services: 服务名称
        :return:
        """
        return list(self.client.get_methods_meta(services).keys())

    # 获取服务的元类
    def services_meta(self, services: str):
        """
        ['CopyToProto', 'FindMethodByName', 'GetOptions', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'file', 'full_name', 'index', 'methods', 'methods_by_name', 'name']

        :param services:
        :return:
        """
        return self.client.get_service_descriptor(services)

    # 获取方法的元类
    def method_meta(self, services: str, methods: str):
        """
        ['CopyToProto', 'GetOptions', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'containing_service', 'full_name', 'index', 'input_type', 'name', 'output_type']

        :param services:
        :param methods:
        :return:
        """
        return self.client.get_method_descriptor(services, methods)

    # 发送grpc 请求，类似request 那种
    def request_services(self, service: str, methods: str, request_data: dict = None):
        """
        :param request_data: 请求参数
        :param service:  具体的服务
        :param methods: 具体的方法
        :return:  返回结果
        """
        response = self.client.request(service, methods, request_data)
        result = json.dumps(response, ensure_ascii=False, indent=2)
        return result


class GrpcStub(object):
    def __init__(self, url: str, module: str, services: str):
        """
        service_descriptor = DESCRIPTOR.services_by_name['SaasService']  # or you can just use _GREETER
        client = StubClient.get_by_endpoint("112.124.46.38:20005", service_descriptors=[service_descriptor, ])
        :param url:
        :param services:
        """
        module = importlib.import_module(module)
        service_descriptor = module.DESCRIPTOR.services_by_name[services]  # or you can just use _GREETER
        self.client = StubClient.get_by_endpoint(url, service_descriptors=[service_descriptor, ])

    def requests_services(self, service_full_name: str, method: str, request_data: dict = None):
        service = self.client.service(service_full_name)
        result = eval('service.{}({})'.format(method, request_data))
        return result


if __name__ == '__main__':
    stub = GrpcStub("localhost:50051", 'demo.hello_pb2', 'Greeter')
    print(stub.requests_services("Greeter", 'Hello', {"name": 'sunshicheng'}))
