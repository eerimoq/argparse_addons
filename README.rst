|buildstatus|_
|coverage|_

About
=====

Additional Python argparse types and actions.

Project homepage: https://github.com/eerimoq/argparse_addons

Installation
============

.. code-block:: text

    $ pip install argparse_addons

Examples
========

Integer range type
------------------

The script. See `examples/integer_range_type.py`_ for the complete
script.

.. code-block:: python

   parser.add_argument('--min-max',
                       type=argparse_addons.IntegerRangeType(0, 255))
   parser.add_argument('--min',
                       type=argparse_addons.IntegerRangeType(0, None))
   parser.add_argument('--max',
                       type=argparse_addons.IntegerRangeType(None, 255))

Error message for the ``--min-max`` argument.

.. code-block:: text

   $ python3 examples/integer_range_type.py --min-max -1
   usage: integer_range_type.py [-h] [--min-max MIN_MAX] [--min MIN] [--max MAX]
   integer_range_type.py: error: argument --min-max: -1 is not in the range 0..255

Error message for the ``--min`` argument.

.. code-block:: text

   $ python3 examples/integer_range_type.py --min -1
   usage: integer_range_type.py [-h] [--min-max MIN_MAX] [--min MIN] [--max MAX]
   integer_range_type.py: error: argument --min: -1 is not in the range 0..inf

Error message for the ``--max`` argument.

.. code-block:: text

   $ python3 examples/integer_range_type.py --max 1000
   usage: integer_range_type.py [-h] [--min-max MIN_MAX] [--min MIN] [--max MAX]
   integer_range_type.py: error: argument --max: 1000 is not in the range -inf..255

All values within allowed ranges.

.. code-block:: text

   $ python3 examples/integer_range_type.py --min-max 47 --min 1000 --max -5
   --min-max: 47
   --min:     1000
   --max:     -5

Contributing
============

#. Fork the repository.

#. Install prerequisites.

   .. code-block:: text

      pip install -r requirements.txt

#. Implement the new feature or bug fix.

#. Implement test case(s) to ensure that future changes do not break
   legacy.

#. Run the tests.

   .. code-block:: text

      make test

#. Create a pull request.

.. |buildstatus| image:: https://travis-ci.com/eerimoq/argparse_addons.svg
.. _buildstatus: https://travis-ci.com/eerimoq/argparse_addons

.. |coverage| image:: https://coveralls.io/repos/github/eerimoq/argparse_addons/badge.svg?branch=master
.. _coverage: https://coveralls.io/github/eerimoq/argparse_addons

.. _examples/integer_range_type.py: https://github.com/eerimoq/argparse_addons/blob/master/examples/integer_range_type.py
