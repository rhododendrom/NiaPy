
__all__ = ['Runner']

class Runner(object):

    def __init__(self, algorithms, benchmarks):
        self.algorithms = algorithms
        self.benchmarks = benchmarks

    @staticmethod
    def run(cls, export):
        