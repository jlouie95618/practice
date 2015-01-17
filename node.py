import os, os.path, sys, math, time

class node():
	"""class for a node object"""
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def __str__(self):
		return str(self.data)
