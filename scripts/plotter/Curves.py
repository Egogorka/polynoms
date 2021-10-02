from typing import List, Callable
from enum import Enum

import numpy

class Curve:

	class Type(Enum):
		DEFAULT = 0
		CLOSED_LOOP = 1
		DISCONNECTED = 2

	def __init__(self, ls, type: Type):
		self.points = ls
		self.type = type

	def transform(self, func: Callable[[complex], complex]):
		for index, point in enumerate(self.points):
			self.points[index] = func(point)

	def transform_smoothly(self, func: Callable[[complex], complex], n: int):
		"""
		:param func: Function that transforms the curve
		:param n: amount of in-between points
		:return: List[Curve] - curves
		"""
		points = []
		for point in self.points:
			point_new = func(point)
			dr = (point_new - point)/n
			points.append([point + i*dr for i in range(n+1)])

		points = [[points[j][i] for j in range(len(points))] for i in range(len(points[0]))]
		curves = [Curve(pts, self.type) for pts in points ]

		return curves
