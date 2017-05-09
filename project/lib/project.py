from process import Process


class Project:

    def __init__(self, options):
        self.options = options
        self.process = Process()

    def date(self):
        self._get_date()

    def _get_date(self):
        print self.process.execute("date")

    def deal_with_arg(self):
        print 'Dealing with %s' % self.options.example
        print 'Version: %s' % self.options.version
