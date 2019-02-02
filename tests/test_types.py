from enum import Enum

import binascii
import pytest
import six
from schematics import Model

from protobuf_schematics.types import EnumType, BytesType


class TestEnumType(object):
    class SomeEnum(Enum):
        A = 1
        B = 2
        C = 3

    class OtherEnum(Enum):
        A = 1

    field = EnumType(SomeEnum)

    def test_to_native(self):
        assert self.field.to_native(self.SomeEnum.A) == self.SomeEnum.A
        assert self.field.to_native('B') == self.SomeEnum.B
        with pytest.raises(KeyError):
            self.field.to_native(self.SomeEnum.A.value)
        with pytest.raises(KeyError):
            self.field.to_native(self.OtherEnum.A)

    def test_to_primitive(self):
        assert self.field.to_primitive(self.SomeEnum.A) == 'A'

        with pytest.raises(TypeError):
            self.field.to_primitive('A')

    def test_mock(self):
        class SomeModel(Model):
            field = EnumType(self.SomeEnum, required=True)

        SomeModel.get_mock_object()


class TestBytesType(object):
    field = BytesType()

    def test_to_native(self):
        assert self.field.to_native(b'123') == b'123'
        assert self.field.to_native('V+zSAA==') == b'W\xec\xd2\x00'

        non_base64_string = 'some-non-base64-string'
        if six.PY3:
            with pytest.raises(binascii.Error):
                self.field.to_native(non_base64_string)
        elif six.PY2:
            assert self.field.to_native(non_base64_string) == non_base64_string

    def test_to_primitive(self):
        assert self.field.to_primitive(b'W\xec\xd2\x00') == 'V+zSAA=='

        with pytest.raises(TypeError):
            self.field.to_primitive(123)

        string_value = 'ABC'
        if six.PY3:
            with pytest.raises(TypeError):
                self.field.to_primitive(string_value)
        elif six.PY2:
            assert self.field.to_primitive(string_value) == 'QUJD'

    def test_mock(self):
        class SomeModel(Model):
            field = BytesType(required=True)

        SomeModel.get_mock_object()

