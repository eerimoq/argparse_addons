import argparse


__version__ = '0.2.0'


class IntegerRangeType:

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def __call__(self, string):
        value = int(string, 0)

        if self.minimum is not None and self.maximum is not None:
            if not self.minimum <= value <= self.maximum:
                raise argparse.ArgumentTypeError(
                    f'{string} is not in the range {self.minimum}..{self.maximum}')
        elif self.minimum is not None:
            if value < self.minimum:
                raise argparse.ArgumentTypeError(
                    f'{string} is not {self.minimum} or higher')
        elif self.maximum is not None:
            if value > self.maximum:
                raise argparse.ArgumentTypeError(
                    f'{string} is not {self.maximum} or lower')

        return value

    def __repr__(self):
        return 'integer'
