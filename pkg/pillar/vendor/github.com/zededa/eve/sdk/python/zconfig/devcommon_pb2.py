# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: devcommon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='devcommon.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x64\x65vcommon.proto\"/\n\x0eUUIDandVersion\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"0\n\x07\x41\x64\x61pter\x12\x17\n\x04type\x18\x01 \x01(\x0e\x32\t.ZCioType\x12\x0c\n\x04name\x18\x02 \x01(\t\"V\n\x0eZcServicePoint\x12\x1e\n\x06zsType\x18\x03 \x01(\x0e\x32\x0e.ZcServiceType\x12\x10\n\x08NameOrIp\x18\x01 \x01(\t\x12\x12\n\nCredential\x18\x02 \x01(\t*\\\n\x08ZCioType\x12\x0b\n\x07ZCioNop\x10\x00\x12\x0b\n\x07ZCioEth\x10\x01\x12\x0b\n\x07ZCioUSB\x10\x02\x12\x0b\n\x07ZCioCOM\x10\x03\x12\x0c\n\x08ZCioHDMI\x10\x04\x12\x0e\n\tZCioOther\x10\xff\x01*G\n\rZcServiceType\x12\x14\n\x10zcloudInvalidSrv\x10\x00\x12\r\n\tmapServer\x10\x01\x12\x11\n\rsupportServer\x10\x02\x42G\n\x1f\x63om.zededa.cloud.uservice.protoZ$github.com/zededa/eve/sdk/go/zconfigb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ZCIOTYPE = _descriptor.EnumDescriptor(
  name='ZCioType',
  full_name='ZCioType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZCioNop', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioEth', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioUSB', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioCOM', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioHDMI', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioOther', index=5, number=255,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=206,
  serialized_end=298,
)
_sym_db.RegisterEnumDescriptor(_ZCIOTYPE)

ZCioType = enum_type_wrapper.EnumTypeWrapper(_ZCIOTYPE)
_ZCSERVICETYPE = _descriptor.EnumDescriptor(
  name='ZcServiceType',
  full_name='ZcServiceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='zcloudInvalidSrv', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='mapServer', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='supportServer', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=300,
  serialized_end=371,
)
_sym_db.RegisterEnumDescriptor(_ZCSERVICETYPE)

ZcServiceType = enum_type_wrapper.EnumTypeWrapper(_ZCSERVICETYPE)
ZCioNop = 0
ZCioEth = 1
ZCioUSB = 2
ZCioCOM = 3
ZCioHDMI = 4
ZCioOther = 255
zcloudInvalidSrv = 0
mapServer = 1
supportServer = 2



_UUIDANDVERSION = _descriptor.Descriptor(
  name='UUIDandVersion',
  full_name='UUIDandVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='UUIDandVersion.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='UUIDandVersion.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=66,
)


_ADAPTER = _descriptor.Descriptor(
  name='Adapter',
  full_name='Adapter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Adapter.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Adapter.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=116,
)


_ZCSERVICEPOINT = _descriptor.Descriptor(
  name='ZcServicePoint',
  full_name='ZcServicePoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zsType', full_name='ZcServicePoint.zsType', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='NameOrIp', full_name='ZcServicePoint.NameOrIp', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Credential', full_name='ZcServicePoint.Credential', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=204,
)

_ADAPTER.fields_by_name['type'].enum_type = _ZCIOTYPE
_ZCSERVICEPOINT.fields_by_name['zsType'].enum_type = _ZCSERVICETYPE
DESCRIPTOR.message_types_by_name['UUIDandVersion'] = _UUIDANDVERSION
DESCRIPTOR.message_types_by_name['Adapter'] = _ADAPTER
DESCRIPTOR.message_types_by_name['ZcServicePoint'] = _ZCSERVICEPOINT
DESCRIPTOR.enum_types_by_name['ZCioType'] = _ZCIOTYPE
DESCRIPTOR.enum_types_by_name['ZcServiceType'] = _ZCSERVICETYPE

UUIDandVersion = _reflection.GeneratedProtocolMessageType('UUIDandVersion', (_message.Message,), dict(
  DESCRIPTOR = _UUIDANDVERSION,
  __module__ = 'devcommon_pb2'
  # @@protoc_insertion_point(class_scope:UUIDandVersion)
  ))
_sym_db.RegisterMessage(UUIDandVersion)

Adapter = _reflection.GeneratedProtocolMessageType('Adapter', (_message.Message,), dict(
  DESCRIPTOR = _ADAPTER,
  __module__ = 'devcommon_pb2'
  # @@protoc_insertion_point(class_scope:Adapter)
  ))
_sym_db.RegisterMessage(Adapter)

ZcServicePoint = _reflection.GeneratedProtocolMessageType('ZcServicePoint', (_message.Message,), dict(
  DESCRIPTOR = _ZCSERVICEPOINT,
  __module__ = 'devcommon_pb2'
  # @@protoc_insertion_point(class_scope:ZcServicePoint)
  ))
_sym_db.RegisterMessage(ZcServicePoint)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\037com.zededa.cloud.uservice.protoZ$github.com/zededa/eve/sdk/go/zconfig'))
# @@protoc_insertion_point(module_scope)