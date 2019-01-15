from typing import TypeVar, Dict

from google.protobuf.json_format import MessageToDict
from google.protobuf.reflection import GeneratedProtocolMessageType
from schematics import Model


T = TypeVar('T', bound='ProtobufMessageModel')


class ProtobufMessageModel(Model):
    @classmethod
    def import_from_protobuf_message(cls, message):  # type: (GeneratedProtocolMessageType) -> T
        instance = cls(MessageToDict(message, preserving_proto_field_name=True, including_default_value_fields=True))
        instance._protobuf_message = message
        return instance

    @property
    def protobuf_message(self):  # type: () -> GeneratedProtocolMessageType
        return self._protobuf_message

    @classmethod
    def import_from_dict(cls, obj):  # type: (Dict) -> T
        return cls(obj)
