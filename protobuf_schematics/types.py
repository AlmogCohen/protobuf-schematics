import random
from base64 import b64decode, b64encode
from random import choice

from schematics.types import StringType


class EnumType(StringType):
    def __init__(self, enum_class, **kwargs):
        self.enum_class = enum_class
        super(EnumType, self).__init__(**kwargs)

    def to_native(self, value, context=None):
        if value in self.enum_class:
            return value
        return self.enum_class[value]

    def to_primitive(self, value, context=None):
        return value.name

    def _mock(self, context=None):
        return choice(list(self.enum_class))


class BytesType(StringType):
    def to_native(self, value, context=None):
        if isinstance(value, bytes):
            return value
        return b64decode(value)

    def to_primitive(self, value, context=None):
        return b64encode(value).decode('ascii')

    def _mock(self, context=None):
        # nasty hack to get the should be size
        size = len(super(BytesType, self)._mock(context))
        return bytes(random.getrandbits(8) for _ in range(size))
