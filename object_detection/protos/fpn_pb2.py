# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/fpn.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!object_detection/protos/fpn.proto\x12\x17object_detection.protos\"i\n\x16\x46\x65\x61turePyramidNetworks\x12\x14\n\tmin_level\x18\x01 \x01(\x05:\x01\x33\x12\x14\n\tmax_level\x18\x02 \x01(\x05:\x01\x37\x12#\n\x16\x61\x64\x64itional_layer_depth\x18\x03 \x01(\x05:\x03\x32\x35\x36\"\xc4\x01\n#BidirectionalFeaturePyramidNetworks\x12\x14\n\tmin_level\x18\x01 \x01(\x05:\x01\x33\x12\x14\n\tmax_level\x18\x02 \x01(\x05:\x01\x37\x12\x16\n\x0enum_iterations\x18\x03 \x01(\x05\x12\x13\n\x0bnum_filters\x18\x04 \x01(\x05\x12&\n\x0e\x63ombine_method\x18\x05 \x01(\t:\x0e\x66\x61st_attention\x12\x1c\n\x14use_native_resize_op\x18\x06 \x01(\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.fpn_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FEATUREPYRAMIDNETWORKS']._serialized_start=62
  _globals['_FEATUREPYRAMIDNETWORKS']._serialized_end=167
  _globals['_BIDIRECTIONALFEATUREPYRAMIDNETWORKS']._serialized_start=170
  _globals['_BIDIRECTIONALFEATUREPYRAMIDNETWORKS']._serialized_end=366
# @@protoc_insertion_point(module_scope)
