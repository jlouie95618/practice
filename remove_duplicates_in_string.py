import os, os.path, sys, math, time
from linkedlist import linkedlist
from node import node

"""
Example Input from commandline:

python remove_duplicates_in_string.py aaappppappplelelelslelelel

Example Output:

l -> e -> l -> e -> l -> e -> l -> s -> l -> e -> l -> e -> l -> e -> l -> p -> p -> p -> a -> p -> p -> p -> p -> a -> a -> a -> None
l -> e -> s -> p -> a -> None

"""

def removeDuplicates(linked_list):
	head = linked_list.head
	while head != None:
		removeDup(head, head, head.next_node)
		head = head.next_node

def removeDup(orig, prev, comp):
	if comp != None:
		if orig.data == comp.data: 
			removeNode(prev, comp)
			removeDup(orig, prev, prev.next_node)
		else: removeDup(orig, comp, comp.next_node)

def removeNode(prev, curr):
	prev.next_node = curr.next_node
	del curr


s = sys.argv[1]

linked_list = linkedlist(node(s[0]))
for i in xrange(1, len(s)):
	linked_list.insert(node(s[i]))

linked_list.printList()

removeDuplicates(linked_list)

linked_list.printList()


