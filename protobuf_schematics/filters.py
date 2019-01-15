"""Define Jinja2 filters used in the templates compilation."""
from pyrobuf import parse_proto


def field_converter(field):  # type: (parse_proto.Parser.Field) -> str
    """Convert a field to it's Schematics representation."""
    if field.token_type == 'MAP_FIELD':
        return _map_field_converter(field)
    else:
        return _regular_field_converter(field)


def _regular_field_converter(field):  # type: (parse_proto.Parser.Field) -> str
    """Convert regular field to it's Schematics representation."""
    if field.type == 'string':
        field_repr = 'StringType()'
    elif field.type == 'uint32' or field.type == 'uint64':
        field_repr = 'IntType()'
    elif field.type == 'bytes':
        field_repr = 'BytesType()'
    elif field.type == 'message':
        field_repr = 'ModelType({})'.format(field.message_name)
    elif field.type == 'enum':
        field_repr = 'EnumType({})'.format(field.enum_def.name)
    else:
        raise ValueError('UNKNOWN FIELD TYPE. Type: {}, Name: {}'.format(field.type, field.name))

    if field.modifier == 'repeated':
        field_repr = 'ListType({})'.format(field_repr)
    return '{} = {}'.format(field.name, field_repr)


def _map_field_converter(field):  # type: (parse_proto.Parser.MapField) -> str
    """Convert map field to it's Schematics representation."""
    if field.type == 'message':
        value = 'ModelType({})'.format(field.message_name)
    elif field.type == 'enum':
        value = 'EnumType({})'.format(field.enum_def.name)
    elif field.type == 'string':
        value = 'StringType()'
    elif field.type == 'uint32' or field.type == 'uint64':
        value = 'IntType()'
    elif field.type == 'bytes':
        value = 'BytesType()'
    else:
        raise ValueError('UNKNOWN VALUE TYPE. Type: {}, Name: {}'.format(field.type, field.name))

    if field.key_type == 'string':
        key = 'str'
    elif field.key_type == 'uint32' or field.key_type == 'uint64':
        key = 'int'
    elif field.key_type == 'bytes':
        key = 'str'
    else:
        raise ValueError('UNKNOWN KEY TYPE. Type: {}, Name: {}'.format(field.type, field.name))

    return '{} = DictType({}, {})'.format(field.name, value, key)
