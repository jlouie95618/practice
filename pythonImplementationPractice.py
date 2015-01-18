import os, os.path, sys, math, time
from linkedlist import linkedlist
from stack import stack
from node import node

""" Lord of the Rings inspiration from my Stanford 106B
	course reader.

"""

def main(args):
	# linkedListTesting(args)
	# stackTesting(args)

	graphTesting(args)



def linkedListTesting(args):
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
	# Error Testing
	print ""
	new_linked_list = linkedlist()
	new_linked_list.search("Minas Tirith")
	new_linked_list.search("foobar")

	# Testing remove functionality
	linked_list.remove("Gondor")
	linked_list.printList()
	# Error testing
	print ""
	linked_list.remove("foobar")
	new_linked_list.remove("Minas Tirith")
	new_linked_list.remove("foobar")
	print linked_list.size
	print new_linked_list.size


	print ""
	linked_list.remove("Minas Tirith")
	linked_list.printList()
	print linked_list.size

	print ""
	linked_list.remove("Rohan")
	linked_list.printList()

def stackTesting(args):
	word_stack = stack()
	print word_stack.isEmpty()
	print word_stack.stackSize()
	for x in xrange(0, len(args)):
		word_stack.push(args[x])

	word_stack.toString()

	print word_stack.isEmpty()

	print word_stack.stackSize()

	print word_stack.pop()

	print word_stack.stackSize()

	word_stack.toString()

	print word_stack.peek()

	word_stack.toString()

	print "about to clear..."
	word_stack.clear()

	word_stack.toString()

	print "is it empty?"
	word_stack.isEmpty()

	print "how large is it?"
	word_stack.size

	word_stack.push("hi")

	word_stack.toString()

def graphTesting(args):
	pass

main(sys.argv)