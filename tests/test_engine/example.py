from enum import Enum

from schematics import Model
from schematics.types import ListType, ModelType, IntType, StringType, DictType


class EnumType(StringType):
    def __init__(self, enum_class, **kwargs):
        self.enum_class = enum_class
        super(EnumType, self).__init__(**kwargs)

    def to_native(self, value, context=None):
        try:
            return self.enum_class[value]
        except KeyError:
            return self.enum_class(value)


class BytesType(StringType):
    pass


class IPAddressFamily(Enum):
    INVALID = 0
    IPv4 = 1
    IPv6 = 2


class ProtocolAndPorts(Model):
    ports = ListType(IntType())


class FlowFilter(Model):
    class InnerEnum(Enum):
        VALUE = 0

    id = StringType()
    consumer_filter_id = EnumType(InnerEnum)
    ports = DictType(ModelType(ProtocolAndPorts), str)
    protocol_and_ports = ListType(ModelType(ProtocolAndPorts))

