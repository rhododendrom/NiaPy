# encoding=utf8
# pylint: disable=mixed-indentation, multiple-statements, line-too-long, logging-not-lazy, no-self-use, attribute-defined-outside-init, arguments-differ, bad-continuation
import logging

from scipy.special import gamma as Gamma
from numpy import where, sin, fabs, pi, full

from NiaPy.algorithms.algorithm import Algorithm

logging.basicConfig()
logger = logging.getLogger('NiaPy.algorithms.basic')
logger.setLevel('INFO')

__all__ = ['FlowerPollinationAlgorithm']

class FlowerPollinationAlgorithm(Algorithm):
	r"""Implementation of Flower Pollination algorithm.

	Algorithm:
		Flower Pollination algorithm

	Date:
		2018

	Authors:
		Dusan Fister, Iztok Fister Jr. and Klemen Berkovič

	License:
		MIT

	Reference paper:
		Yang, Xin-She. "Flower pollination algorithm for global optimization. International conference on unconventional computing and natural computation. Springer, Berlin, Heidelberg, 2012.

	References URL:
		Implementation is based on the following MATLAB code: https://www.mathworks.com/matlabcentral/fileexchange/45112-flower-pollination-algorithm?requestedDomain=true

	Attributes:
		Name (List[str]): List of strings representing algorithm names.
		p (float): probability switch.
		beta (float): TODO.

	See Also:
		:class:`NiaPy.algorithms.algorithm.Algorithm`
	"""
	Name = ['FlowerPollinationAlgorithm', 'FPA']

	@staticmethod
	def typeParameters():
		r"""TODO.

		Returns:
			Dict[str, Callable]:
				* p (function): TODO
				* beta (function): TODO

		See Also:
			:func:`NiaPy.algorithms.algorithm.Algorithm.typeParameters`
		"""
		d = Algorithm.typeParameters()
		d.update({
			'p': lambda x: isinstance(x, float) and 0 <= x <= 1,
			'beta': lambda x: isinstance(x, (float, int)) and x > 0,
		})
		return d

	def setParameters(self, NP=25, p=0.35, beta=1.5, **ukwargs):
		r"""Set core parameters of FlowerPollinationAlgorithm algorithm.

		Arguments:
			NP (int): Population size.
			p (float): Probability switch.
			beta (float): TODO.

		See Also:
			:func:`NiaPy.algorithms.algorithm.Algorithm.setParameters`
		"""
		Algorithm.setParameters(self, NP=NP)
		self.p, self.beta = p, beta
		if ukwargs: logger.info('Unused arguments: %s' % (ukwargs))

	def repair(self, x, task):
		r"""Repair solution to search space.

		Args:
			x (numpy.ndarray): Solution to fix.
			task (Task): Optimization task.

		Returns:
			numpy.ndarray: fixed solution.
		"""
		ir = where(x > task.Upper)
		x[ir] = task.Lower[ir] + x[ir] % task.bRange[ir]
		ir = where(x < task.Lower)
		x[ir] = task.Lower[ir] + x[ir] % task.bRange[ir]
		return x

	def levy(self):
		r"""Levy function.

		Returns:
			float: Next Levy number.
		"""
		sigma = (Gamma(1 + self.beta) * sin(pi * self.beta / 2) / (Gamma(1 + self.beta) * self.beta * 2 ** ((self.beta - 1) / 2))) ** (1 / self.beta)
		return 0.01 * (self.normal(0, 1) * sigma / fabs(self.normal(0, 1)) ** (1 / self.beta))

	def runIteration(self, task, Sol, Sol_f, xb, fxb, **dparams):
		r"""Core function of FlowerPollinationAlgorithm algorithm.

		Args:
			task (Task): Optimization task.
			Sol (numpy.ndarray): Current population.
			Sol_f (numpy.ndarray[float]): Current population fitness/function values.
			xb (numpy.ndarray): Global best solution.
			fxb (float): Global best solution function/fitness value.
			**dparams (Dict[str, Any]): Additional arguments.

		Returns:
			Tuple[numpy.ndarray, numpy.ndarray[float], Dict[str, Any]]:
				1. New population.
				2. New populations fitness/function values.
				3. Additional arguments.
		"""
		for i in range(self.NP):
			S = full(task.D, 0.0)
			if self.uniform(0, 1) > self.p: S += self.levy() * (Sol[i] - xb)
			else:
				JK = self.Rand.permutation(self.NP)
				S += self.uniform(0, 1) * (Sol[JK[0]] - Sol[JK[1]])
			S = self.repair(S, task)
			f_i = task.eval(S)
			if f_i <= Sol_f[i]: Sol[i], Sol_f[i] = S, f_i
		return Sol, Sol_f, {}

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
