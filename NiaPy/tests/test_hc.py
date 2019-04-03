# encoding=utf8
# pylint: disable=mixed-indentation, multiple-statements
from NiaPy.tests.test_algorithm import AlgorithmTestCase, MyBenchmark
from NiaPy.algorithms.other import HillClimbAlgorithm

class HCTestCase(AlgorithmTestCase):
	def test_custom_works_fine(self):
		ihc_custom = HillClimbAlgorithm(delta=0.4, seed=self.seed)
		ihc_customc = HillClimbAlgorithm(delta=0.4, seed=self.seed)
		AlgorithmTestCase.algorithm_run_test(self, ihc_custom, ihc_customc, MyBenchmark())

	def test_griewank_works_fine(self):
		ihc_griewank = HillClimbAlgorithm(seed=self.seed)
		ihc_griewankc = HillClimbAlgorithm(seed=self.seed)
		AlgorithmTestCase.algorithm_run_test(self, ihc_griewank, ihc_griewankc)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
