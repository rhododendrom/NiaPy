# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

import random
from NiaPy.algorithms.modified import SelfAdaptiveDifferentialEvolutionAlgorithm


for i in range(10):
    Algorithm = SelfAdaptiveDifferentialEvolutionAlgorithm(10, 40, 10000, 'sphere')
    Best = Algorithm.run()

    print(Best)
