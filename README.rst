Validator
#########

Validator is a library that provides an improved handling of validation.

The following parts of validation are handled;

    - state
    - transistion


Installation
============

.. code-block:: bash
   pip install etools-validator


Setup
=====

Add ``validator`` to ``INSTALLED_APPS`` in ``settings.py``

.. code-block:: python
   INSTALLED_APPS = [
       ...
       'validator',
   ]


Usage
=====

Use ``validator`` in views

..  code-block:: python
   from validator.mixins import ValidatorViewMixin

   class ExampleView(ValidatorViewMixin, ListCreateAPIView):
       ...


Contributing
============

Environment Setup
-----------------

To install the necessary libraries

::

   $ pip install -r requirements/dev.txt


Coding Standards
----------------

See `PEP 8 Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_ for complete details on the coding standards.

To run checks on the code to ensure code is in compliance

::

   $ flake8 .


Testing
-------

Testing is important and tests are located in `tests/` directory and can be run with;

::

   $ coverage run manage.py test

Coverage report is viewable in `build/coverage` directory, and can be generated with;

::

   $ coverage html
