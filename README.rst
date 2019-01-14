===================
ProtoBuf Schematics
===================


.. image:: https://img.shields.io/pypi/v/protobuf_schematics.svg
        :target: https://pypi.python.org/pypi/protobuf_schematics

.. image:: https://img.shields.io/travis/AlmogCohen/protobuf_schematics.svg
        :target: https://travis-ci.org/AlmogCohen/protobuf-schematics

.. image:: https://readthedocs.org/projects/protobuf-schematics/badge/?version=latest
        :target: https://protobuf-schematics.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Convert ProtoBuf ``proto`` file to cute Schematics_ classes file.

Google Protobuf is great when it comes to high performance schema aware APIs, but when Google designed Protobuf, it didn't tried to make the generated code idiomatic in Python, which brings a problem when exporting messages outside interface modules or having nice IDE auto-completions. Schematics is a cute and Pythonic schema library that goes well with most applications. Why not join both?

Currently this package does **not** support the Protobuf binary format and will work with a any other textual representation which is easily generated with the original Protobuf API for any language. Ease of use was prioritized while writing this package rather than mere performance.


* Free software: Apache Software License 2.0
* Documentation: https://protobuf-schematics.readthedocs.io.


.. _Schematics: https://github.com/schematics/schematics

Usage
-----

1. Convert the ``proto`` file to python Schematics_ classes::

    protobuf_schematics <path-to-file.proto> generated_schematics_proto.py # or any output filename

2. Convert your ProtoBuf message to Json:

In Java:

.. code:: java

    import com.google.protobuf.util.JsonFormat;

    FileWriter file = new FileWriter("protoBufMessage.json")
    JsonFormat.Printer printer = JsonFormat.printer().preservingProtoFieldNames();
    String message = printer.print(someProtoBufMessage);
    file.write(message)

or from Python:

.. code:: python

    import json
    from google.protobuf.json_format import MessageToJson

    json = MessageToJson(org, preserving_proto_field_name=True)
    with open("protoBufMessage.json", 'w') as output:
        json.dump(json, output)

3. In your project, load the message in python as Schematics_ object:

.. code:: python

    import json
    from generated_schematics_proto import SomeClass # import the schematics message class

    schematics_root_message = SomeClass(json.load(open('protoBufMessage.json')))


Example
-------

This ``proto`` file:

.. code-block:: proto

    syntax = "proto3";

    enum IPAddressFamily {
        INVALID = 0;
        IPv4 = 1;
        IPv6 = 2;
    };

    message ProtocolAndPorts {
        repeated uint32 ports = 3;
    }

    message FlowFilter {
        enum InnerEnum {
            VALUE = 0;
        };
        string id = 1 [deprecated = true];
        InnerEnum consumer_filter_id = 2;
        map<string, ProtocolAndPorts> ports = 3;
        repeated ProtocolAndPorts protocol_and_ports = 4;
    }

Will be converted to:

.. code-block:: python3

    class IPAddressFamily(Enum):
        INVALID = 0
        IPv4 = 1
        IPv6 = 2


    class ProtocolAndPorts(Model):
        ports = ListType(IntType())


    class FlowFilter(Model):
        class InnerEnum(Enum):
            VALUE = 0

        id = StringType()
        consumer_filter_id = EnumType(InnerEnum)
        ports = DictType(ModelType(ProtocolAndPorts), str)
        protocol_and_ports = ListType(ModelType(ProtocolAndPorts))


Features
--------

* Support both Protobuf syntax 2 and 3.
* Support builtin types such as StringType, ``IntType``.
* Support proto map fields as Schematics_ ``DictType``.
* Support ``repeated`` modifier as convert to ``ListType``.
* Support Enum class generation and custom Schematics ``EnumType``.
* Support custom schematics ``ByteArrayType`` base64 encoded byte arrays converted from Java.

Development
-----------

First, install the Pipfile and create the proper virtual environment::

    pipenv install --dev

To check linting with **flake8**, run::

    make lint

To run the unittests against your working python version::

    py.test

To see coverage report::

    make coverage

To run tests against all supported python versions::

    tox

To make the docs (which will be automatically published to readthedocs on commits to the master branch)::

    make docs

Credits
-------

The parsing work of **.proto** files is provided thanks to the awesome guys at PyroBuf_.

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elgertam/cookiecutter-pipenv`: https://github.com/elgertam/cookiecutter-pipenv
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _PyroBuf: https://github.com/appnexus/pyrobuf
