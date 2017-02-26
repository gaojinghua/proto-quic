# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: isolate_bot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='isolate_bot.proto',
  package='luci.swarming.bot',
  syntax='proto3',
  serialized_pb=_b('\n\x11isolate_bot.proto\x12\x11luci.swarming.bot\"C\n\x0f\x43ontainsRequest\x12\x30\n\x06\x64igest\x18\x01 \x03(\x0b\x32 .luci.swarming.bot.ContentDigest\">\n\rContainsReply\x12-\n\x06status\x18\x01 \x01(\x0b\x32\x1d.luci.swarming.bot.BlobStatus\">\n\x10PushBlobsRequest\x12*\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1c.luci.swarming.bot.BlobChunk\"?\n\x0ePushBlobsReply\x12-\n\x06status\x18\x01 \x01(\x0b\x32\x1d.luci.swarming.bot.BlobStatus\"E\n\x11\x46\x65tchBlobsRequest\x12\x30\n\x06\x64igest\x18\x01 \x03(\x0b\x32 .luci.swarming.bot.ContentDigest\"l\n\x0f\x46\x65tchBlobsReply\x12-\n\x06status\x18\x01 \x01(\x0b\x32\x1d.luci.swarming.bot.BlobStatus\x12*\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1c.luci.swarming.bot.BlobChunk\"[\n\tBlobChunk\x12\x30\n\x06\x64igest\x18\x01 \x01(\x0b\x32 .luci.swarming.bot.ContentDigest\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"D\n\rContentDigest\x12\x0e\n\x06\x64igest\x18\x01 \x01(\x0c\x12\x12\n\nsize_bytes\x18\x02 \x01(\x03\x12\x0f\n\x07version\x18\x03 \x01(\x05\"\x80\x02\n\nBlobStatus\x12\x11\n\tsucceeded\x18\x01 \x01(\x08\x12\x36\n\x05\x65rror\x18\x02 \x01(\x0e\x32\'.luci.swarming.bot.BlobStatus.ErrorCode\x12\x14\n\x0c\x65rror_detail\x18\x03 \x01(\t\x12\x38\n\x0emissing_digest\x18\x04 \x03(\x0b\x32 .luci.swarming.bot.ContentDigest\"W\n\tErrorCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x14\n\x10INVALID_ARGUMENT\x10\x01\x12\x12\n\x0eMISSING_DIGEST\x10\x02\x12\x13\n\x0f\x44IGEST_MISMATCH\x10\x03\x32\x90\x02\n\x0b\x46ileService\x12P\n\x08\x43ontains\x12\".luci.swarming.bot.ContainsRequest\x1a .luci.swarming.bot.ContainsReply\x12U\n\tPushBlobs\x12#.luci.swarming.bot.PushBlobsRequest\x1a!.luci.swarming.bot.PushBlobsReply(\x01\x12X\n\nFetchBlobs\x12$.luci.swarming.bot.FetchBlobsRequest\x1a\".luci.swarming.bot.FetchBlobsReply0\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BLOBSTATUS_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='luci.swarming.bot.BlobStatus.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ARGUMENT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_DIGEST', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIGEST_MISMATCH', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=816,
  serialized_end=903,
)
_sym_db.RegisterEnumDescriptor(_BLOBSTATUS_ERRORCODE)


_CONTAINSREQUEST = _descriptor.Descriptor(
  name='ContainsRequest',
  full_name='luci.swarming.bot.ContainsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digest', full_name='luci.swarming.bot.ContainsRequest.digest', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=40,
  serialized_end=107,
)


_CONTAINSREPLY = _descriptor.Descriptor(
  name='ContainsReply',
  full_name='luci.swarming.bot.ContainsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='luci.swarming.bot.ContainsReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=109,
  serialized_end=171,
)


_PUSHBLOBSREQUEST = _descriptor.Descriptor(
  name='PushBlobsRequest',
  full_name='luci.swarming.bot.PushBlobsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='luci.swarming.bot.PushBlobsRequest.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=173,
  serialized_end=235,
)


_PUSHBLOBSREPLY = _descriptor.Descriptor(
  name='PushBlobsReply',
  full_name='luci.swarming.bot.PushBlobsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='luci.swarming.bot.PushBlobsReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=237,
  serialized_end=300,
)


_FETCHBLOBSREQUEST = _descriptor.Descriptor(
  name='FetchBlobsRequest',
  full_name='luci.swarming.bot.FetchBlobsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digest', full_name='luci.swarming.bot.FetchBlobsRequest.digest', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=302,
  serialized_end=371,
)


_FETCHBLOBSREPLY = _descriptor.Descriptor(
  name='FetchBlobsReply',
  full_name='luci.swarming.bot.FetchBlobsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='luci.swarming.bot.FetchBlobsReply.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='luci.swarming.bot.FetchBlobsReply.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=373,
  serialized_end=481,
)


_BLOBCHUNK = _descriptor.Descriptor(
  name='BlobChunk',
  full_name='luci.swarming.bot.BlobChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digest', full_name='luci.swarming.bot.BlobChunk.digest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='luci.swarming.bot.BlobChunk.offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='luci.swarming.bot.BlobChunk.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=483,
  serialized_end=574,
)


_CONTENTDIGEST = _descriptor.Descriptor(
  name='ContentDigest',
  full_name='luci.swarming.bot.ContentDigest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digest', full_name='luci.swarming.bot.ContentDigest.digest', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size_bytes', full_name='luci.swarming.bot.ContentDigest.size_bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='luci.swarming.bot.ContentDigest.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=576,
  serialized_end=644,
)


_BLOBSTATUS = _descriptor.Descriptor(
  name='BlobStatus',
  full_name='luci.swarming.bot.BlobStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='succeeded', full_name='luci.swarming.bot.BlobStatus.succeeded', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='luci.swarming.bot.BlobStatus.error', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_detail', full_name='luci.swarming.bot.BlobStatus.error_detail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missing_digest', full_name='luci.swarming.bot.BlobStatus.missing_digest', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BLOBSTATUS_ERRORCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=647,
  serialized_end=903,
)

_CONTAINSREQUEST.fields_by_name['digest'].message_type = _CONTENTDIGEST
_CONTAINSREPLY.fields_by_name['status'].message_type = _BLOBSTATUS
_PUSHBLOBSREQUEST.fields_by_name['data'].message_type = _BLOBCHUNK
_PUSHBLOBSREPLY.fields_by_name['status'].message_type = _BLOBSTATUS
_FETCHBLOBSREQUEST.fields_by_name['digest'].message_type = _CONTENTDIGEST
_FETCHBLOBSREPLY.fields_by_name['status'].message_type = _BLOBSTATUS
_FETCHBLOBSREPLY.fields_by_name['data'].message_type = _BLOBCHUNK
_BLOBCHUNK.fields_by_name['digest'].message_type = _CONTENTDIGEST
_BLOBSTATUS.fields_by_name['error'].enum_type = _BLOBSTATUS_ERRORCODE
_BLOBSTATUS.fields_by_name['missing_digest'].message_type = _CONTENTDIGEST
_BLOBSTATUS_ERRORCODE.containing_type = _BLOBSTATUS
DESCRIPTOR.message_types_by_name['ContainsRequest'] = _CONTAINSREQUEST
DESCRIPTOR.message_types_by_name['ContainsReply'] = _CONTAINSREPLY
DESCRIPTOR.message_types_by_name['PushBlobsRequest'] = _PUSHBLOBSREQUEST
DESCRIPTOR.message_types_by_name['PushBlobsReply'] = _PUSHBLOBSREPLY
DESCRIPTOR.message_types_by_name['FetchBlobsRequest'] = _FETCHBLOBSREQUEST
DESCRIPTOR.message_types_by_name['FetchBlobsReply'] = _FETCHBLOBSREPLY
DESCRIPTOR.message_types_by_name['BlobChunk'] = _BLOBCHUNK
DESCRIPTOR.message_types_by_name['ContentDigest'] = _CONTENTDIGEST
DESCRIPTOR.message_types_by_name['BlobStatus'] = _BLOBSTATUS

ContainsRequest = _reflection.GeneratedProtocolMessageType('ContainsRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINSREQUEST,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.ContainsRequest)
  ))
_sym_db.RegisterMessage(ContainsRequest)

ContainsReply = _reflection.GeneratedProtocolMessageType('ContainsReply', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINSREPLY,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.ContainsReply)
  ))
_sym_db.RegisterMessage(ContainsReply)

PushBlobsRequest = _reflection.GeneratedProtocolMessageType('PushBlobsRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUSHBLOBSREQUEST,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.PushBlobsRequest)
  ))
_sym_db.RegisterMessage(PushBlobsRequest)

PushBlobsReply = _reflection.GeneratedProtocolMessageType('PushBlobsReply', (_message.Message,), dict(
  DESCRIPTOR = _PUSHBLOBSREPLY,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.PushBlobsReply)
  ))
_sym_db.RegisterMessage(PushBlobsReply)

FetchBlobsRequest = _reflection.GeneratedProtocolMessageType('FetchBlobsRequest', (_message.Message,), dict(
  DESCRIPTOR = _FETCHBLOBSREQUEST,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.FetchBlobsRequest)
  ))
_sym_db.RegisterMessage(FetchBlobsRequest)

FetchBlobsReply = _reflection.GeneratedProtocolMessageType('FetchBlobsReply', (_message.Message,), dict(
  DESCRIPTOR = _FETCHBLOBSREPLY,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.FetchBlobsReply)
  ))
_sym_db.RegisterMessage(FetchBlobsReply)

BlobChunk = _reflection.GeneratedProtocolMessageType('BlobChunk', (_message.Message,), dict(
  DESCRIPTOR = _BLOBCHUNK,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.BlobChunk)
  ))
_sym_db.RegisterMessage(BlobChunk)

ContentDigest = _reflection.GeneratedProtocolMessageType('ContentDigest', (_message.Message,), dict(
  DESCRIPTOR = _CONTENTDIGEST,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.ContentDigest)
  ))
_sym_db.RegisterMessage(ContentDigest)

BlobStatus = _reflection.GeneratedProtocolMessageType('BlobStatus', (_message.Message,), dict(
  DESCRIPTOR = _BLOBSTATUS,
  __module__ = 'isolate_bot_pb2'
  # @@protoc_insertion_point(class_scope:luci.swarming.bot.BlobStatus)
  ))
_sym_db.RegisterMessage(BlobStatus)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class FileServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Contains = channel.unary_unary(
        '/luci.swarming.bot.FileService/Contains',
        request_serializer=ContainsRequest.SerializeToString,
        response_deserializer=ContainsReply.FromString,
        )
    self.PushBlobs = channel.stream_unary(
        '/luci.swarming.bot.FileService/PushBlobs',
        request_serializer=PushBlobsRequest.SerializeToString,
        response_deserializer=PushBlobsReply.FromString,
        )
    self.FetchBlobs = channel.unary_stream(
        '/luci.swarming.bot.FileService/FetchBlobs',
        request_serializer=FetchBlobsRequest.SerializeToString,
        response_deserializer=FetchBlobsReply.FromString,
        )


class FileServiceServicer(object):

  def Contains(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushBlobs(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchBlobs(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Contains': grpc.unary_unary_rpc_method_handler(
          servicer.Contains,
          request_deserializer=ContainsRequest.FromString,
          response_serializer=ContainsReply.SerializeToString,
      ),
      'PushBlobs': grpc.stream_unary_rpc_method_handler(
          servicer.PushBlobs,
          request_deserializer=PushBlobsRequest.FromString,
          response_serializer=PushBlobsReply.SerializeToString,
      ),
      'FetchBlobs': grpc.unary_stream_rpc_method_handler(
          servicer.FetchBlobs,
          request_deserializer=FetchBlobsRequest.FromString,
          response_serializer=FetchBlobsReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'luci.swarming.bot.FileService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaFileServiceServicer(object):
  def Contains(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def PushBlobs(self, request_iterator, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def FetchBlobs(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaFileServiceStub(object):
  def Contains(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Contains.future = None
  def PushBlobs(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  PushBlobs.future = None
  def FetchBlobs(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_FileService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('luci.swarming.bot.FileService', 'Contains'): ContainsRequest.FromString,
    ('luci.swarming.bot.FileService', 'FetchBlobs'): FetchBlobsRequest.FromString,
    ('luci.swarming.bot.FileService', 'PushBlobs'): PushBlobsRequest.FromString,
  }
  response_serializers = {
    ('luci.swarming.bot.FileService', 'Contains'): ContainsReply.SerializeToString,
    ('luci.swarming.bot.FileService', 'FetchBlobs'): FetchBlobsReply.SerializeToString,
    ('luci.swarming.bot.FileService', 'PushBlobs'): PushBlobsReply.SerializeToString,
  }
  method_implementations = {
    ('luci.swarming.bot.FileService', 'Contains'): face_utilities.unary_unary_inline(servicer.Contains),
    ('luci.swarming.bot.FileService', 'FetchBlobs'): face_utilities.unary_stream_inline(servicer.FetchBlobs),
    ('luci.swarming.bot.FileService', 'PushBlobs'): face_utilities.stream_unary_inline(servicer.PushBlobs),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_FileService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('luci.swarming.bot.FileService', 'Contains'): ContainsRequest.SerializeToString,
    ('luci.swarming.bot.FileService', 'FetchBlobs'): FetchBlobsRequest.SerializeToString,
    ('luci.swarming.bot.FileService', 'PushBlobs'): PushBlobsRequest.SerializeToString,
  }
  response_deserializers = {
    ('luci.swarming.bot.FileService', 'Contains'): ContainsReply.FromString,
    ('luci.swarming.bot.FileService', 'FetchBlobs'): FetchBlobsReply.FromString,
    ('luci.swarming.bot.FileService', 'PushBlobs'): PushBlobsReply.FromString,
  }
  cardinalities = {
    'Contains': cardinality.Cardinality.UNARY_UNARY,
    'FetchBlobs': cardinality.Cardinality.UNARY_STREAM,
    'PushBlobs': cardinality.Cardinality.STREAM_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'luci.swarming.bot.FileService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)