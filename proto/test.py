"""
Author    : Mr. Sun.
FileName  : test.py
Time      : 2021/12/27 2:25 PM
Desc      :

TYPE_DOUBLE         = 1
  TYPE_FLOAT          = 2
  TYPE_INT64          = 3
  TYPE_UINT64         = 4
  TYPE_INT32          = 5
  TYPE_FIXED64        = 6
  TYPE_FIXED32        = 7
  TYPE_BOOL           = 8
  TYPE_STRING         = 9
  TYPE_GROUP          = 10
  TYPE_MESSAGE        = 11
  TYPE_BYTES          = 12
  TYPE_UINT32         = 13
  TYPE_ENUM           = 14
  TYPE_SFIXED32       = 15
  TYPE_SFIXED64       = 16
  TYPE_SINT32         = 17
  TYPE_SINT64         = 18
  MAX_TYPE            = 18

['CPPTYPE_BOOL', 'CPPTYPE_DOUBLE', 'CPPTYPE_ENUM', 'CPPTYPE_FLOAT', 'CPPTYPE_INT32', 'CPPTYPE_INT64', 'CPPTYPE_MESSAGE', 'CPPTYPE_STRING', 'CPPTYPE_UINT32', 'CPPTYPE_UINT64', 'GetOptions', 'LABEL_OPTIONAL', 'LABEL_REPEATED', 'LABEL_REQUIRED', 'TYPE_BOOL', 'TYPE_BYTES', 'TYPE_DOUBLE', 'TYPE_ENUM', 'TYPE_FIXED32', 'TYPE_FIXED64', 'TYPE_FLOAT', 'TYPE_GROUP', 'TYPE_INT32', 'TYPE_INT64', 'TYPE_MESSAGE', 'TYPE_SFIXED32', 'TYPE_SFIXED64', 'TYPE_SINT32', 'TYPE_SINT64', 'TYPE_STRING', 'TYPE_UINT32', 'TYPE_UINT64', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_cdescriptor', '_options', '_serialized_options', 'camelcase_name', 'containing_oneof', 'containing_type', 'cpp_type', 'default_value', 'enum_type', 'extension_scope', 'file', 'full_name', 'has_default_value', 'has_options', 'id', 'index', 'is_extension', 'json_name', 'label', 'message_type', 'name', 'number', 'type']

"""
import saas_pb2

msg = saas_pb2.GetStaffInfoRequest()
name = msg.DESCRIPTOR.fields[0].name
type_ = msg.DESCRIPTOR.fields[0].type
print(name, type_)
msg1 = saas_pb2.GetStaffInfoResponse()
name_length = len(msg1.DESCRIPTOR.fields)
for i in range(name_length):
    print(msg1.DESCRIPTOR.fields[i].name, msg1.DESCRIPTOR.fields[i].type, msg1.DESCRIPTOR.fields[i].message_type)

# type_1 = msg1.DESCRIPTOR.fields[0].type
# print(name1, type_1)

 # meta = client.method_meta('saas.SaasService', 'GetStaffInfo')
    # print(dir(meta))
    # print(meta.name)
    # print(dir(meta.input_type))
    # print(meta.input_type.name)
    # print(meta.input_type.fields.__len__)
    # print(meta.input_type.fields[0].name, meta.input_type.fields[0].type)
    # print(dir(meta.input_type.fields))
    # print(dir(meta.input_type.fields))
    # print(meta.input_type.fields.count,meta.input_type.fields.index)
    # print(meta.input_type, meta.output_type)
    # print(dir(_message.Message))
