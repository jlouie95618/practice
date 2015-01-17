import os, os.path, sys, math, time
from node import node

class linkedlist():
	""" Implementing a class for a linked list. Elements will be inserted at the beginning of the linked list every time.
	   	Important Methods that have been implemented:
	   		-insert
	   		-remove
	   		-search
	   		-printList"""


	def __init__(self, first_node = None):
		# the head is a node object passed in from program
		self.head = first_node

	def insert(self, new_node):
		if self.head == None:
			# if the "head" was not initialized 
			#	at the initialization of the list
			self.head = new_node
		else:
			# setting the new node's next to curr head
			new_node.next_node = self.head
			# replace reference to head with new_node
			self.head = new_node

	def search(self, data, flag = False):
		# Check to make sure the linked list is not empty
		if self.head == None:
			print "List has not been given a node yet."
			# return None for client error checking
			return None
		else:
			# obtain head node in order to traverse list
			curr = self.head
			while curr != None:
				# if 
				if curr.data == data: return curr
				curr = curr.next_node
			print "A node with the given data could not be found."
			return None

	def remove(self, data = None):
		pass

	def printList(self):
		curr = self.head
		str_rep = ""
		while curr != None:
			str_rep += (str(curr) + " -> ")
			curr = curr.next_node
		str_rep += "None"
		print str_rep
