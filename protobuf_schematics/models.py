from typing import TypeVar, Dict

from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.reflection import GeneratedProtocolMessageType
from schematics import Model

T = TypeVar('T', bound='ProtobufMessageModel')


class ProtobufMessageModel(Model):
    def __init__(self, *args, **kwargs):
        super(ProtobufMessageModel, self).__init__(*args, **kwargs)
        self._protobuf_message = None

    @classmethod
    def import_from_protobuf_message(cls, message):  # type: (GeneratedProtocolMessageType) -> T
        instance = cls(MessageToDict(message, preserving_proto_field_name=True, including_default_value_fields=True))
        instance._protobuf_message = message
        return instance

    def export_into_protobuf_message(self, message):
        # type: (GeneratedProtocolMessageType) -> GeneratedProtocolMessageType
        """
        Export the contents of this model into a given protobuf message.

        Args:
            message: Initialized protobuf message on which this model definition was based.

        Returns:
            The same protobuf message, populated with the data from this model.
        """
        return ParseDict(self.to_primitive(), message)

    @property
    def protobuf_message(self):  # type: () -> GeneratedProtocolMessageType
        assert self._protobuf_message is not None, \
            'Original protobuf message missing as this model was not initialized from a protobuf message.'
        return self._protobuf_message

    @classmethod
    def import_from_dict(cls, obj):  # type: (Dict) -> T
        return cls(obj)
