import os, os.path, sys, math, time
from linkedlist import linkedlist
from node import node

"""
THIS NEEDS A LOT OF DEBUGGING HELP... :/
"""

def partition(linked_list, x):
	head = linked_list.head
	next_node = head.next_node
	while next_node != None:
		if next_node.data > x:
			head = bubble(next_node, next_node.next_node, head)
			next_node = next_node.next_node
		elif next_node.data < x:
			linked_list.printList()
			head = bubble(next_node.next_node, next_node, head)

def bubble(down, up, head):
	if up != None:
		up.next_node = down.next_node
	if down != None:
		down.next_node = head
		return down


s = sys.argv[1]

x = sys.argv[2]

linked_list = linkedlist(node(s[0]))
for i in xrange(1, len(s)):
	linked_list.insert(node(s[i]))

linked_list.printList()

partition(linked_list, x)

linked_list.printList()