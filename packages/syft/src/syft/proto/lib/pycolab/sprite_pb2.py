# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/pycolab/sprite.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.lib.numpy import array_pb2 as proto_dot_lib_dot_numpy_dot_array__pb2
from syft.proto.lib.python import tuple_pb2 as proto_dot_lib_dot_python_dot_tuple__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/pycolab/sprite.proto",
    package="syft.lib.pycolab",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1eproto/lib/pycolab/sprite.proto\x12\x10syft.lib.pycolab\x1a\x1bproto/lib/numpy/array.proto\x1a\x1cproto/lib/python/tuple.proto"\x96\x03\n\x06Sprite\x12\x10\n\x08obj_type\x18\x01 \x01(\t\x12\x16\n\tcharacter\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07visible\x18\x03 \x01(\x08H\x01\x88\x01\x01\x12\x19\n\x0chas_position\x18\x04 \x01(\x08H\x02\x88\x01\x01\x12\x31\n\x08position\x18\x05 \x01(\x0b\x32\x1a.syft.lib.numpy.NumpyProtoH\x03\x88\x01\x01\x12\x17\n\nhas_corner\x18\x06 \x01(\x08H\x04\x88\x01\x01\x12+\n\x06\x63orner\x18\x07 \x01(\x0b\x32\x16.syft.lib.python.TupleH\x05\x88\x01\x01\x12\x18\n\x0bhas_curtain\x18\x08 \x01(\x08H\x06\x88\x01\x01\x12\x30\n\x07\x63urtain\x18\t \x01(\x0b\x32\x1a.syft.lib.numpy.NumpyProtoH\x07\x88\x01\x01\x42\x0c\n\n_characterB\n\n\x08_visibleB\x0f\n\r_has_positionB\x0b\n\t_positionB\r\n\x0b_has_cornerB\t\n\x07_cornerB\x0e\n\x0c_has_curtainB\n\n\x08_curtainb\x06proto3',
    dependencies=[
        proto_dot_lib_dot_numpy_dot_array__pb2.DESCRIPTOR,
        proto_dot_lib_dot_python_dot_tuple__pb2.DESCRIPTOR,
    ],
)


_SPRITE = _descriptor.Descriptor(
    name="Sprite",
    full_name="syft.lib.pycolab.Sprite",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="obj_type",
            full_name="syft.lib.pycolab.Sprite.obj_type",
            index=0,
            number=1,
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
            name="character",
            full_name="syft.lib.pycolab.Sprite.character",
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
            name="visible",
            full_name="syft.lib.pycolab.Sprite.visible",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="has_position",
            full_name="syft.lib.pycolab.Sprite.has_position",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="position",
            full_name="syft.lib.pycolab.Sprite.position",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="has_corner",
            full_name="syft.lib.pycolab.Sprite.has_corner",
            index=5,
            number=6,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="corner",
            full_name="syft.lib.pycolab.Sprite.corner",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="has_curtain",
            full_name="syft.lib.pycolab.Sprite.has_curtain",
            index=7,
            number=8,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
            name="curtain",
            full_name="syft.lib.pycolab.Sprite.curtain",
            index=8,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    oneofs=[
        _descriptor.OneofDescriptor(
            name="_character",
            full_name="syft.lib.pycolab.Sprite._character",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_visible",
            full_name="syft.lib.pycolab.Sprite._visible",
            index=1,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_has_position",
            full_name="syft.lib.pycolab.Sprite._has_position",
            index=2,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_position",
            full_name="syft.lib.pycolab.Sprite._position",
            index=3,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_has_corner",
            full_name="syft.lib.pycolab.Sprite._has_corner",
            index=4,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_corner",
            full_name="syft.lib.pycolab.Sprite._corner",
            index=5,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_has_curtain",
            full_name="syft.lib.pycolab.Sprite._has_curtain",
            index=6,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_curtain",
            full_name="syft.lib.pycolab.Sprite._curtain",
            index=7,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=112,
    serialized_end=518,
)

_SPRITE.fields_by_name[
    "position"
].message_type = proto_dot_lib_dot_numpy_dot_array__pb2._NUMPYPROTO
_SPRITE.fields_by_name[
    "corner"
].message_type = proto_dot_lib_dot_python_dot_tuple__pb2._TUPLE
_SPRITE.fields_by_name[
    "curtain"
].message_type = proto_dot_lib_dot_numpy_dot_array__pb2._NUMPYPROTO
_SPRITE.oneofs_by_name["_character"].fields.append(_SPRITE.fields_by_name["character"])
_SPRITE.fields_by_name["character"].containing_oneof = _SPRITE.oneofs_by_name[
    "_character"
]
_SPRITE.oneofs_by_name["_visible"].fields.append(_SPRITE.fields_by_name["visible"])
_SPRITE.fields_by_name["visible"].containing_oneof = _SPRITE.oneofs_by_name["_visible"]
_SPRITE.oneofs_by_name["_has_position"].fields.append(
    _SPRITE.fields_by_name["has_position"]
)
_SPRITE.fields_by_name["has_position"].containing_oneof = _SPRITE.oneofs_by_name[
    "_has_position"
]
_SPRITE.oneofs_by_name["_position"].fields.append(_SPRITE.fields_by_name["position"])
_SPRITE.fields_by_name["position"].containing_oneof = _SPRITE.oneofs_by_name[
    "_position"
]
_SPRITE.oneofs_by_name["_has_corner"].fields.append(
    _SPRITE.fields_by_name["has_corner"]
)
_SPRITE.fields_by_name["has_corner"].containing_oneof = _SPRITE.oneofs_by_name[
    "_has_corner"
]
_SPRITE.oneofs_by_name["_corner"].fields.append(_SPRITE.fields_by_name["corner"])
_SPRITE.fields_by_name["corner"].containing_oneof = _SPRITE.oneofs_by_name["_corner"]
_SPRITE.oneofs_by_name["_has_curtain"].fields.append(
    _SPRITE.fields_by_name["has_curtain"]
)
_SPRITE.fields_by_name["has_curtain"].containing_oneof = _SPRITE.oneofs_by_name[
    "_has_curtain"
]
_SPRITE.oneofs_by_name["_curtain"].fields.append(_SPRITE.fields_by_name["curtain"])
_SPRITE.fields_by_name["curtain"].containing_oneof = _SPRITE.oneofs_by_name["_curtain"]
DESCRIPTOR.message_types_by_name["Sprite"] = _SPRITE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sprite = _reflection.GeneratedProtocolMessageType(
    "Sprite",
    (_message.Message,),
    {
        "DESCRIPTOR": _SPRITE,
        "__module__": "proto.lib.pycolab.sprite_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.pycolab.Sprite)
    },
)
_sym_db.RegisterMessage(Sprite)


# @@protoc_insertion_point(module_scope)