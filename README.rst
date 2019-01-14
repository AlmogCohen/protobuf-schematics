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
