import os, os.path, sys, math, time
from node import node

""" Within this module, I've attempted to implement multiple kinds of graph
	representations, some of which include:
		-Adjacent list
		-Adjacent matrix
"""

class graph_adjl():
	"""Implementation of an adjacent list graph"""
	def __init__(self, head = None):
		self.head = head
		self.num_nodes = 1
		self.num_arcs = 0

class graph_adjm():
	"""Implementaiton of an adjacent matrix graph"""
	def __init__(self, head = None):
		self.head = head
		self.num_nodes = 1
		self.num_arcs = 0
		
