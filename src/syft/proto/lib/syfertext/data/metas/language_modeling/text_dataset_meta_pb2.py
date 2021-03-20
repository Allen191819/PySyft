# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/syfertext/data/metas/language_modeling/text_dataset_meta.proto

# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/syfertext/data/metas/language_modeling/text_dataset_meta.proto",
    package="syft.lib.syfertext",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nHproto/lib/syfertext/data/metas/language_modeling/text_dataset_meta.proto\x12\x12syft.lib.syfertext"Z\n\x0fTextDatasetMeta\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x12\n\ntrain_path\x18\x02 \x01(\t\x12\x12\n\nvalid_path\x18\x03 \x01(\t\x12\x11\n\ttest_path\x18\x04 \x01(\tb\x06proto3',
)


_TEXTDATASETMETA = _descriptor.Descriptor(
    name="TextDatasetMeta",
    full_name="syft.lib.syfertext.TextDatasetMeta",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uuid",
            full_name="syft.lib.syfertext.TextDatasetMeta.uuid",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="train_path",
            full_name="syft.lib.syfertext.TextDatasetMeta.train_path",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="valid_path",
            full_name="syft.lib.syfertext.TextDatasetMeta.valid_path",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="test_path",
            full_name="syft.lib.syfertext.TextDatasetMeta.test_path",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=96,
    serialized_end=186,
)

DESCRIPTOR.message_types_by_name["TextDatasetMeta"] = _TEXTDATASETMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextDatasetMeta = _reflection.GeneratedProtocolMessageType(
    "TextDatasetMeta",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXTDATASETMETA,
        "__module__": "proto.lib.syfertext.data.metas.language_modeling.text_dataset_meta_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.syfertext.TextDatasetMeta)
    },
)
_sym_db.RegisterMessage(TextDatasetMeta)


# @@protoc_insertion_point(module_scope)