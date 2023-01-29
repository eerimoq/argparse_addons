import unittest
import argparse
import argparse_addons


class ArgparseAddonsTest(unittest.TestCase):

    def test_integer(self):
        integer = argparse_addons.Integer()

        self.assertEqual(integer('0'), 0)
        self.assertEqual(integer('0x1a'), 0x1a)

        with self.assertRaises(ValueError):
            integer('ab')

    def test_integer_min_and_max(self):
        integer = argparse_addons.Integer(0, 255)

        self.assertEqual(integer('0'), 0)
        self.assertEqual(integer('255'), 255)

        with self.assertRaises(argparse.ArgumentTypeError) as cm:
            integer('-1')

        self.assertEqual(str(cm.exception), '-1 is not in the range 0..255')

        with self.assertRaises(argparse.ArgumentTypeError) as cm:
            integer('256')

        self.assertEqual(str(cm.exception), '256 is not in the range 0..255')

        with self.assertRaises(ValueError):
            integer('foobar')

    def test_integer_min(self):
        integer = argparse_addons.Integer(0, None)

        self.assertEqual(integer('0'), 0)
        self.assertEqual(integer('100000'), 100000)

        with self.assertRaises(argparse.ArgumentTypeError) as cm:
            integer('-1')

        self.assertEqual(str(cm.exception), '-1 is not in the range 0..inf')

    def test_integer_max(self):
        integer = argparse_addons.Integer(None, 5)

        self.assertEqual(integer('5'), 5)
        self.assertEqual(integer('-111'), -111)

        with self.assertRaises(argparse.ArgumentTypeError) as cm:
            integer('6')

        self.assertEqual(str(cm.exception), '6 is not in the range -inf..5')

    def test_integer_repr(self):
        self.assertEqual(repr(argparse_addons.Integer(0, 1)), 'integer')

    def test_integer_hex(self):
        integer = argparse_addons.Integer(0, 5)

        self.assertEqual(integer('0x1'), 1)

    def test_parse_log_level(self):
        levels = argparse_addons.parse_log_level('info')
        self.assertEqual(levels, [(None, 'info')])

        levels = argparse_addons.parse_log_level('foo=info')
        self.assertEqual(levels, [('foo', 'info')])

        levels = argparse_addons.parse_log_level('foo=info:bar=debug')
        self.assertEqual(levels,
                         [
                             ('foo', 'info'),
                             ('bar', 'debug')
                         ])

        levels = argparse_addons.parse_log_level('foo,fie=kalle:bar=debug:debug')
        self.assertEqual(levels,
                         [
                             ('foo', 'kalle'),
                             ('fie', 'kalle'),
                             ('bar', 'debug'),
                             (None, 'debug')
                         ])
