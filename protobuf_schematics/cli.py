# -*- coding: utf-8 -*-

"""Console script for protobuf_schematics."""
import sys
import click

from protobuf_schematics.engine import parse_proto_file, compile_parser_result


@click.command()
@click.argument('proto_path', type=click.Path(exists=True, readable=True, dir_okay=False, resolve_path=True))
@click.argument('output_path', type=click.Path(writable=True))
def main(proto_path, output_path):
    """
    Create schematics definitions file from a proto file

    Args:
        proto_path: Input path to the `.proto` file.
        output_path: Output path for the schematics definitions file.

    Returns:
        int: 0 upon successful execution.
    """
    parser_result = parse_proto_file(proto_path)
    schematics_code = compile_parser_result(parser_result)
    with open(output_path, 'w') as output:
        output.write(schematics_code)
    print("Done! Successfully written to {}".format(output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
