import os, os.path, sys, math, time
from node import node, graphnode

class graph(object):
	"""docstring for simple graph"""
	def __init__(self, head = None):
		self.head = head
		self.num_nodes = 1
		self.num_arcs = 0

		