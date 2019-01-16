from enum import Enum

from schematics import Model
from schematics.types import ListType, ModelType, IntType, StringType, DictType

from protobuf_schematics.models import ProtobufMessageModel
from protobuf_schematics.types import EnumType, BytesType


class IPAddressFamily(Enum):
    INVALID = 0
    IPv4 = 1
    IPv6 = 2


class ProtocolAndPorts(ProtobufMessageModel):
    ports = ListType(IntType())


class FlowFilter(ProtobufMessageModel):
    class SomeEnum(Enum):
        VALUE = 0

    id = StringType()
    consumer_filter_id = EnumType(SomeEnum)
    ports = DictType(ModelType(ProtocolAndPorts), str)
    protocol_and_ports = ListType(ModelType(ProtocolAndPorts))

