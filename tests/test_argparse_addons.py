import unittest
import argparse
import argparse_addons


class ArgparseAddonsTest(unittest.TestCase):

    def test_integer_range_type_min_and_max(self):
        integer_range_type = argparse_addons.IntegerRangeType(0, 255)

        self.assertEqual(integer_range_type('0'), 0)
        self.assertEqual(integer_range_type('255'), 255)

        with self.assertRaises(argparse.ArgumentTypeError) as cm:
            integer_range_type('-1')

        self.assertEqual(str(cm.exception), '-1 is not in the range 0..255')

        with self.assertRaises(argparse.ArgumentTypeError) as cm:
            integer_range_type('256')

        self.assertEqual(str(cm.exception), '256 is not in the range 0..255')

        with self.assertRaises(ValueError):
            integer_range_type('foobar')

    def test_integer_range_type_min(self):
        integer_range_type = argparse_addons.IntegerRangeType(0, None)

        self.assertEqual(integer_range_type('0'), 0)
        self.assertEqual(integer_range_type('100000'), 100000)

        with self.assertRaises(argparse.ArgumentTypeError) as cm:
            integer_range_type('-1')

        self.assertEqual(str(cm.exception), '-1 is not in the range 0..inf')

    def test_integer_range_type_max(self):
        integer_range_type = argparse_addons.IntegerRangeType(None, 5)

        self.assertEqual(integer_range_type('5'), 5)
        self.assertEqual(integer_range_type('-111'), -111)

        with self.assertRaises(argparse.ArgumentTypeError) as cm:
            integer_range_type('6')

        self.assertEqual(str(cm.exception), '6 is not in the range -inf..5')

    def test_integer_range_type_repr(self):
        self.assertEqual(repr(argparse_addons.IntegerRangeType(0, 1)), 'integer')

    def test_integer_range_type_hex(self):
        integer_range_type = argparse_addons.IntegerRangeType(0, 5)

        self.assertEqual(integer_range_type('0x1'), 1)
