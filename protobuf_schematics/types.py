from base64 import b64decode, b64encode

from schematics.types import StringType


class EnumType(StringType):
    def __init__(self, enum_class, **kwargs):
        self.enum_class = enum_class
        super(EnumType, self).__init__(**kwargs)

    def to_native(self, value, context=None):
        return self.enum_class[value]

    def to_primitive(self, value, context=None):
        return value.name


class BytesType(StringType):
    def to_native(self, value, context=None):
        return b64decode(value)

    def to_primitive(self, value, context=None):
        return b64encode(value).decode('ascii')
