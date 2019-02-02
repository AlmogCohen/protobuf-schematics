import random
from base64 import b64decode, b64encode
from random import choice

import six
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
        try:
            assert isinstance(value, self.enum_class)
        except AssertionError:
            raise TypeError('EnumType require a proper enum to convert to primitive.')
        return value.name

    def _mock(self, context=None):
        return choice(list(self.enum_class))


class BytesType(StringType):
    def to_native(self, value, context=None):
        if six.PY2:
            try:
                return value.decode('base64')
            except Exception:
                return value
        else:
            if isinstance(value, bytes):
                return value
            return b64decode(value)

    def to_primitive(self, value, context=None):
        return b64encode(value).decode('ascii')

    def _mock(self, context=None):
        # nasty hack to get the should be size
        size = len(super(BytesType, self)._mock(context))
        return bytes(random.getrandbits(8) for _ in range(size))
