import os, os.path, sys, math, time
from node import node

class queue():
	""" Implementing a class for a queue. Elements will be inserted at the 
		end of the linked list every time (LILO). It is important to 
		note that the stack implementation is very similar to that of a 
		linked list; however, a queue is like a simple line of people
	   	Important Methods that have been implemented:
	   		-queue = put an element in as the bottom most value
	   		-dequeue = take off the top most element
	   		-isEmpty = boolean value to deterime if stack is empty or not
	   		-size = returns the number of elements
	   		-peek = reveals value of the top most element (first in)
	   		-clear = removes all the elements within the stack
	   		-toString = print the current queue as a string for debugging"""
	def __init__(self):
		self.first_elem = None
		self.last_elem = None
		self.size = 0

