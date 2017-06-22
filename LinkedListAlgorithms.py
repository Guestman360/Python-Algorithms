# singly linked list

class Node(object):
	def __init__(self, val):
		self.value = val
		self.nextnode = None  # since it is a singly linked list only worry about next node


#IMPORTANT to set up the nodes and their values
a = Node(1)
b = Node(2)
c = Node(3)
#IMPORTANT set up the order of the list, in this case it is circular
a.nextnode = b
b.nextnode = c
c.nextnode = a
print(a.value)

#Singly Linked list Cycle Check - algorithm problem
#Check if last node points to first, circular linked list

def cycle_check(node):

	marker1 = node #both "racers" start at the line
	marker2 = node

	while marker2 != None and marker2.nextnode != None: #As long as there is an actual node & not an empty one

		marker1 = marker1.nextnode
		marker2 = marker2.nextnode.nextnode #marker2 is a little faster, eventually will lap marker1, signifies this
											#is a circular linked list

		if marker2 == marker1: #only if marker2 "laps" marker1
			return  True

	return False

#call funtion and only put one input, in this case a, funtion will then check the rest, this should output 'True'
print(cycle_check(a))

# singly linked list has 0(1) time insertion and deletion, different from search and access which is 0(K)
# from head to K element - as opposed to array where it is 0(1) since you can get the index

#Reverse Linked List in place

def reverse(head):

	current = head
	previous = None
	nextnode = None

	while current:

		nextnode = current.nextnode #head = a, so a nextnode is b, None = b, nextnode = b
		print("nextnode",nextnode)
		current.nextnode = previous #previous has none so previous = b, current.nextnode b = None
		print("current.nextnode",current.nextnode)
		previous = current #previous b = current a, previous = a
		print("previous",previous)
		current = nextnode #a = b, current = b
		print("current",current)

	return  previous #a

# print(reverse(a))
# print("Reversing Here")
# print(a.nextnode.value)
# print(b.nextnode.value)
# print(c.nextnode.value)
#prints a=3,b=1,c=2 -> b = head, c , a = tail
#with tuple unpacking
def Reverse(head):
	prev, curr = None, head
	while curr:
		prev, curr.next, curr = curr, prev, curr.next
	return prev

#Doubly linked list

class DoublyLinkedListNode(object):

	def __init__(self, value):

		self.value = value
		self.next_node = None
		self.prev_node = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.nextnode = b
b.prev_node = a

b.next_node = c
c.prev_node = b

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.nextnode = B
B.nextnode = C
C.nextnode = D
D.nextnode = E
E.nextnode = A


def nth_to_last_node(n, head):
#The block starts at the head
	left_pointer = head
	right_pointer = head
#for loop is for setting up right_pointer n nodes away to form this block
	for i in range(n-1):

		if not right_pointer.nextnode: #if not none
			return "Error man"
			#raise LookupError('Error: n is larger than the linked list')

		right_pointer = right_pointer.nextnode

	while right_pointer.nextnode: #while not none
		#after right and left are set up, increments them until the right is none
		left_pointer = left_pointer.nextnode
		right_pointer = right_pointer.nextnode

	return left_pointer #this will be at nth to last node
	print(left_pointer)

print(nth_to_last_node(3,A))

def greatest_difference(nums):

	sorted_nums = sorted(nums) #dont forget to calculte the big o of utility function like sort
	return sorted_nums[-1] - sorted_nums[0] #-1 means last item in array
#0(n * log2(n)) n is for nums and log2(n) is for sorted funtion
#see if you can do better becasue the sorted adds to n, still better than n2

print(greatest_difference([1,5,8,99,12]))


def greatest_difference2(nums): #this version operates in 0(n) time, becasue we are just looping through array

	max = nums[0]
	min = nums[0]

	for num in nums:
		if num > max:
			max = num
		elif num < max:
			min = num

	return max - min

#practice implementing a single and doubly linked list

class Node(object):

	def __init__(self,value):
		self.value = value
		self.nextnode = None

	### Doubly linked list, same but with a previous var
	def __init__(self,value):
		self.value = value
		self.nextnode = None
		self.previous = None

# a.Node(30)
# b.Node(40)
# c.Node(50)
# d.Node(60)
# e.Node(30)
# f.Node(40)
# g.Node(50)
# h.Node(60)
#
# a.nextnode = b
# b.nextnode = c
# c.nextnode = d
# d.nextnode = e
# e.nextnode = f
# f.nextnode = g
# g.nextnode = h


#Reverse a Linked List with k
def reverseLL(head,k):
	current = head
	next = None
	prev = None
	count = 0

	#Reversing linked list here
	while(current is not None and count < k):
		next = current.next
		current.next = prev
		prev = current
		current = next
		count += 1

	# next is now a pointer to (k+1)th node
		# recursively call for the list starting
		# from current . And make rest of the list as
		# next of first node
	if next is not None:
		head.next = self.reverseLL(next,k) #Recursion resets the count and able to keep reversing

	#prev is the new head of the linkedlist
	return prev

'''
Given Linked List
1 2 3 4 5 6 7 8 9
Reversed list
3 2 1 6 5 4 9 8 7
'''

print("Reverse with K",reverseLL(a.head,3))

#http://jelices.blogspot.com/2014/05/leetcode-python-reverse-nodes-in-k-group.html
#https://crackinterviewtoday.wordpress.com/2010/03/24/reverse-a-single-linked-list-recursive-procedure/
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param k, an integer
	# @return a ListNode
	def reverseKGroup(self, head, k):
		dummy = ListNode(0);
		dummy.next = head
		previous = dummy
		while True:
			begin = previous.next
			end = previous
			for i in range(0,k):
				end = end.next
				if end == None:
					return dummy.next
			nextGroup = end.next
			self.reverseList(begin,end)
			previous.next = end
			begin.next = nextGroup
			previous = begin

	def reverseList(self, start, end):
		alreadyReversed = start
		actual = start
		nextNode = start.next
		while actual != end:
			actual = nextNode
			nextNode = nextNode.next
			actual.next = alreadyReversed
			alreadyReversed = actual

l1 = Node(2)
l1b = Node(4)
l1c = Node(3)

l2 = Node(5)
l2b = Node(6)
l2c = Node(4)

def addTwoNumbers(self, l1, l2):
	carry = 0
	root = n = ListNode(0)
	while l1 or l2 or carry:
		v1 = v2 = 0
		if l1:
			v1 = l1.value
			l1 = l1.next
		if l2:
			v2 = l2.value
			l2 = l2.next
		carry, val = divmod(v1+v2+carry, 10)
		n.next = ListNode(val) #creates a new linkedlist with the new added value
		n = n.next
		print(root.next)
	return root.next

print(addTwoNumbers(l1,l2))

#Recursive version
class MyLinkedList(LinkedList):

	def _add_reverse(self, first_node, second_node, carry):
		# Base case
		if first_node is None and second_node is None and not carry:
			return None

		# Recursive case
		value = carry #assign carry to variable called value
		value += first_node.data if first_node is not None else 0 #add the 1st and 2nd node to value
		value += second_node.data if second_node is not None else 0
		carry = 1 if value >= 10 else 0 #equals 1 if over 1, this is the carry in addition we simulate
		value %= 10 #get the rmainder by % by 10, ex: 14 % 10 = 4
		node = Node(value) #start off a node here, add to it below
		node.next = self._add_reverse( #recurse by going next value in first and second linked list
			first_node.next if first_node is not None else None,
			second_node.next if first_node is not None else None,
			carry) #maintain the current carry and whatever value it contains at that time
		return node

	def add_reverse(self, first_list, second_list): #helper function that uses the previous
		# See constraints
		if first_list is None or second_list is None:
			return None
		head = self._add_reverse(first_list.head, second_list.head, 0)
		return MyLinkedList(head)
