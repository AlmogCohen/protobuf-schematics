#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `protobuf_schematics` package."""

import pytest

from click.testing import CliRunner

from protobuf_schematics import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface(tmp_path):
    """Test the CLI."""

    proto_file_path = str(tmp_path / 'input.proto')
    with open(proto_file_path, 'w') as f:
        f.write("""
syntax = "proto3";

message FlowFilter {
  string id = 1;
}
        """)

    output_file_path = str(tmp_path / 'output.py')

    runner = CliRunner()
    result = runner.invoke(cli.main, args=(proto_file_path, output_file_path))
    assert result.exit_code == 0
    assert result.output.startswith('Done! Successfully written to {}'.format(output_file_path))
    with open(output_file_path, 'r') as f:
        output = f.read()
    output_class = """
class FlowFilter(Model):
    id = StringType()
"""
    assert output_class in output


def test_command_line_help(tmp_path):
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
