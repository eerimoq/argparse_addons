import argparse


__version__ = '0.6.0'


class Integer:

    def __init__(self, minimum=None, maximum=None):
        self.minimum = minimum
        self.maximum = maximum

    def __call__(self, string):
        value = int(string, 0)

        if self.minimum is not None and self.maximum is not None:
            if not self.minimum <= value <= self.maximum:
                raise argparse.ArgumentTypeError(
                    '{} is not in the range {}..{}'.format(string, self.minimum, self.maximum))
        elif self.minimum is not None:
            if value < self.minimum:
                raise argparse.ArgumentTypeError(
                    '{} is not in the range {}..inf'.format(string, self.minimum))
        elif self.maximum is not None:
            if value > self.maximum:
                raise argparse.ArgumentTypeError(
                    '{} is not in the range -inf..{}'.format(string, self.maximum))

        return value

    def __repr__(self):
        return 'integer'
