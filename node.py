import os, os.path, sys, math, time

class node():
	"""general node object for storing data and next node"""
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def __str__(self):
		return str(self.data)
