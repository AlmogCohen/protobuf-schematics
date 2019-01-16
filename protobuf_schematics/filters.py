"""Define Jinja2 filters used in the templates compilation."""
from pyrobuf import parse_proto
from schematics.types import StringType, IntType, ModelType

from protobuf_schematics.types import BytesType, EnumType


class FieldConverter(object):

    PROTOBUF_FIELD_TO_SCHEMATICS_FIELD = {
        'string': StringType,
        'uint32': IntType,
        'uint64': IntType,
        'bytes': BytesType,
        'message': ModelType,
        'enum': EnumType,
    }

    @classmethod
    def convert(cls, field):  # type: (parse_proto.Parser.Field) -> str
        """Convert a field to it's Schematics representation."""
        token_type_to_handler = {
            'MAP_FIELD': cls._map_field_converter,
            'FIELD': cls._regular_field_converter,
        }
        try:
            return token_type_to_handler[field.token_type](field)
        except KeyError:
            raise ValueError('Unsupported Pyrobuf field token type: {}'.format(field.token_type))

    @classmethod
    def _get_pyrobuf_field_repr(cls, field):
        """Return the Schematics string representation of a Pyrobuf field type."""
        try:
            schematics_type = cls.PROTOBUF_FIELD_TO_SCHEMATICS_FIELD[field.type]
        except KeyError:
            raise ValueError('Unsupported Pyrobuf field type: {}. Field name: {}'.format(field.type, field.name))

        type_name = schematics_type.__name__
        arg = ''
        if schematics_type == ModelType:
            arg = field.message_name
        elif schematics_type == EnumType:
            arg = field.enum_def.name
        return '{}({})'.format(type_name, arg)

    @classmethod
    def _regular_field_converter(cls, field):  # type: (parse_proto.Parser.Field) -> str
        """Convert regular field to it's Schematics representation."""
        field_repr = cls._get_pyrobuf_field_repr(field)
        if field.modifier == 'repeated':
            field_repr = 'ListType({})'.format(field_repr)
        return '{} = {}'.format(field.name, field_repr)

    @classmethod
    def _map_field_converter(cls, field):  # type: (parse_proto.Parser.MapField) -> str
        """Convert map field to it's Schematics representation."""
        value = cls._get_pyrobuf_field_repr(field)
        if field.key_type == 'string':
            key = 'str'
        elif field.key_type == 'uint32' or field.key_type == 'uint64':
            key = 'int'
        elif field.key_type == 'bytes':
            key = 'str'
        else:
            raise ValueError(
                'Unsupported type for map field key. Key type: {}, Field name: {}'.format(field.type, field.name)
            )
        return '{} = DictType({}, {})'.format(field.name, value, key)
