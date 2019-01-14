"""Utilities used to compile proto files."""
from jinja2 import Environment, PackageLoader
from pyrobuf.parse_proto import Parser


def parse_proto_file(file_path):
    """
    Returns parsed representation of a `.proto` file.

    Args:
        file_path (str): The file path of the `.proto` file.

    Returns:
        dict: Parsing result from the pyrobuf parser.
    """
    return Parser.parse_from_filename(file_path, None, disabled_tokens=[])


def compile_parser_result(parser_dict):
    """
    Returns schematics representation of a parsed `.proto` file.

    Args:
         parser_dict (dict): The output of the pyrobuf parser.

    Returns:
        str: Representation of the messages as python schematics classes.

    """
    _env = Environment(loader=PackageLoader('protobuf_schematics', 'templates'))
    schematics_template = _env.get_template('schematics_py.tmpl')
    return schematics_template.render(parser_dict=parser_dict)
