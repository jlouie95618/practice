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


	def remove(self, data = None, node = None):
		# find the node BEFORE desired node
		if data != None:
			prev = self.search(data, True)
			prev.next_node = (prev.next_node).next_node
		# if given the desired node to be removed
		#	just replace the node with the next
		elif node != None:
			node = node.next_node
		else:
			print "You are not trying to remove anything."

	def search(self, data, flag = False): # Returns the node containing the desired data
		curr = self.head
		print "head node data: " + self.head.data
		print "data to find: " + data
		if flag == True:
			prev = None
			while curr.data != data:
				if curr.next_node == None: break
				prev = curr
				curr = curr.next_node
			return prev
		else:
			while curr.next_node != None:
				if curr.data == data: return curr
				curr = curr.next_node
		print "Could not find element!" 


	def printList(self):
		curr = self.head
		str_rep = ""
		while curr != None:
			str_rep += (str(curr) + " -> ")
			curr = curr.next_node
		str_rep += "None"
		print str_rep
