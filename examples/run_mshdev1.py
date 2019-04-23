# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

from NiaPy.algorithms.modified import MultiStrategyDifferentialEvolutionMTSv1
from NiaPy.algorithms.basic.de import CrossCurr2Best1, CrossBest1
from NiaPy.task.Task import StoppingTask, OptimizationType
from NiaPy.benchmarks import Sphere

# we will run Differential Evolution for 5 independent runs
for i in range(5):
	task = StoppingTask(D=10, nFES=5000, optType=OptimizationType.MINIMIZATION, benchmark=Sphere())
	algo = MultiStrategyDifferentialEvolutionMTSv1(NP=70, F=0.5, CR=0.4, strategies=(CrossBest1, CrossCurr2Best1))
	best = algo.run(task=task)
	print('%s -> %s' % (best[0].x, best[1]))

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
