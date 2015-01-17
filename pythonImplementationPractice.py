import os, os.path, sys, math, time
from linkedlist import linkedlist
from node import node

""" Lord of the Rings inspiration from my Stanford 106B
	course reader.

"""

def main(args):
	print args
	# Initialize a head node
	head = node("Minas Tirith")
	# Initialize an instance of a linked list
	linked_list = linkedlist(head)
	# Test out adding new node
	new_node = node("Gondor")
	linked_list.insert(new_node)
	# quick check...
	linked_list.printList()


	linked_list.insert(node("Rohan"))


	linked_list.printList()


	# Testing search functionality
	if linked_list.search("Minas Tirith") != None:
		print "Found!"
	linked_list.search("foobar")
	new_linked_list = linkedlist()
	new_linked_list.search("Minas Tirith")
	new_linked_list.search("foobar")

	# Testing remove functionality
	linked_list.remove("Gondor")
	linked_list.printList()


main(sys.argv)