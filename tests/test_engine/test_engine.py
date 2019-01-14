from coverage.annotate import os
from pytest import fixture

from protobuf_schematics.engine import parse_proto_file, compile_parser_result


@fixture
def current_dir(tmpdir, request):
    filename = request.module.__file__
    return os.path.dirname(filename)


@fixture
def example_proto_file(current_dir):
    return os.path.join(current_dir, 'example.proto')


@fixture
def example_output_file_contents(current_dir):
    with open(os.path.join(current_dir, 'example.py')) as f:
        return f.read()


def test_engine(example_proto_file, example_output_file_contents):
    """Test that an input proto is properly compiled to output python classes"""
    result = parse_proto_file(example_proto_file)
    python_classes_file_contents = compile_parser_result(result)

    assert python_classes_file_contents == example_output_file_contents
