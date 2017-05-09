from argparse import ArgumentParser


class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/project'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument(
            '-e',
            '--example',
            '---also-work',
            default='default-value',
            dest='example', # attribute name
            help='Description of this argument'
        )

        self.parser.add_argument(
            '-v',
            '--vsersion',
            dest='version', # attribute name
            default='1.0.0',
            help='help version'
        )

    def parse(self, args=None):
        return self.parser.parse_args(args)
