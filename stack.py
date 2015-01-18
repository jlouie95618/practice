import os, os.path, sys, math, time
from node import node

class stack():
	""" Implementing a class for a stack. Elements will be inserted at the 
		beginning of the linked list every time (LIFO). It is important to 
		note that the stack implementation is very similar to that of a 
		linked list.
	   	Important Methods that have been implemented:
	   		-push = put an element in as the top most value
	   		-pop = take off the top most element
	   		-isEmpty = boolean value to deterime if stack is empty or not
	   		-size = returns the number of elements
	   		-peek = reveals value of the top most element (most recent in)
	   		-clear = removes all the elements within the stack
	   		-toString = print the current stack as a string for debugging"""
	def __init__(self):
		self.top_elem = None
		self.size = 0

	def push(self, data):
		if self.top_elem == None:
			self.top_elem = node(data)
			(self.top_elem).next_node = None
		else:
			new_node = node(data)
			(new_node).next_node = (self.top_elem)
			self.top_elem = new_node
		self.size += 1


	def pop(self):
		value = (self.top_elem).data
		self.top_elem = (self.top_elem).next_node
		self.size -= 1
		return value

	def isEmpty(self):
		if self.size == 0: return True
		else: return False

	def stackSize(self):
		return self.size

	def peek(self):
		return (self.top_elem).data

	def clear(self):
		while self.top_elem != None:
			self.pop()


	def toString(self):
		if self.top_elem != None:
			curr = self.top_elem
			str_rep = ""
			while curr != None:
				str_rep += (str(curr) + " -> ")
				curr = curr.next_node
			str_rep += "None"
			print str_rep
		else: print "Empty stack."
		