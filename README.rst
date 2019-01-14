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




Generate Pythonic Schematics_ representation of ProtoBuf .proto files.

The motive behind it is to create a comfortable mapping in Python to work with ProtoBuf messages represented in JSON or any other serializable form.

Most of the existing interfaces I've found optimize for performance and (apparently) a hellish pythonic interface. This package come to solve that by translating to ProtoBuf **.proto** files to nice and clean Schematics_ models. The hellish ProtoBuf API is converted in the awesome and fluent Schematics_ flow.

**Notice**: Performance was not considered while developing this package.


* Free software: Apache Software License 2.0
* Documentation: https://protobuf-schematics.readthedocs.io.


.. _Schematics: https://github.com/schematics/schematics

Features
--------

* TODO


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
