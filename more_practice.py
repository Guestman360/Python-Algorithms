# import Stack
# import Node
# import BinaryTreeNode
#from pythonds.graphs import Graph

'''
top down - imagine breaking down something into small pieces and deriving solution from that, possibly recursion
bottom up - imagine putting pieces together to build up the solution, i.e. coin problem
'''

#Making Change coin problem, most efficient bottoms up approach with DP
amount = 5
denominations = [1,3,5]
#creates array of amount(5) + 1 = 6 [0,1,2,3,4,5,6] indexes, must find number of ways of making certain coins
#2 ways to make 3, (3) and (1,1,1) 3 ways to make 5, (5), (3,1,1) and (1,1,1,1,1)
#array also includes irrelevant numbers like 4 which arent in origianl array, 2 ways to make 4...
def change_possibilities_bottom_up(amount, denominations):
	ways_of_doing_n_cents = [0] * (amount + 1)
	ways_of_doing_n_cents[0] = 1

	for coin in denominations:
		for higher_amount in range(coin, amount + 1):
			higher_amount_remainder = higher_amount - coin
			print("higher_amount_remainder - the indexes",higher_amount_remainder)
			ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
			print("ways",ways_of_doing_n_cents)

	return ways_of_doing_n_cents[amount]

print(change_possibilities_bottom_up(amount,denominations))
'''
O(n∗m) time and O(n) additional space, where n is the amount of money and m
is the number of potential denominations.
'''

#Find 2nd largest element in BST - O(h) h is height of tree
def find_largest(root_node):
	current = root_node
	while current:
		#If no more right nodes, get value of root, this is the 2nd largest
		if not current.right:
			return current.value
		current = current.right

def find_second_largest(root_node):
	if root_node is None or \
			(root_node.left is None and root_node.right is None):
		raise Exception('Tree must have at least 2 nodes')

	current = root_node

	while current:
		# case: current is largest and has a left subtree
		# 2nd largest is the largest in that subtree
		'''
					5
				   / \
				  3   9 <-- largest!!!
					 /
					7
				   / \
				  6   8 <-- 2nd largest!!!
		'''
		if current.left and not current.right:
			return find_largest(current.left)

		# case: current is parent of largest, and largest has no children,
		# so current is 2nd largest
		if current.right and \
		   not current.right.left and \
		   not current.right.right:
			return current.value

		current = current.right

#Reverse Linked list

#Finding integer complement - 50(1110001) -> 37(0001110) for example
def getIntegerComplement(n):
	mask = (1 << n.bit_length()) - 1
	return n ^ mask

#https://github.com/shellyan/bluewolf
#https://www.reddit.com/r/CS_Questions/comments/mbkl0/duplicate_missing_integer_in_a_large_array/
def findDuplicate(array):

	sortedArray = sorted(array)
	duplicate = sortedArray[0]
	for item in sortedArray[1:]:
		if duplicate == item:
			return duplicate
		duplicate = item #duplicate switches over to current item and is then checked again

#findDuplicate in array of million items - bluewolf
# inputArr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,25,27,28,29,30]
# def findDup(inputArr):
# 	n = len(inputArr)
# 	dsn = n*(n+1)//2
# 	dsn2 = dsn*(2*n+1)//3
# 	i = 0
# 	for num in inputArr:
# 		if i < n:
# 			dsn -= inputArr[num]
# 			dsn2 -= inputArr[num]*inputArr[num]
# 			i += 1
# 		else:
# 			return (dsn2-dsn*dsn)//(2*dsn)
#
# print(findDup(inputArr))

#Word Graph
def buildGraph(wordFile):
	d = {}
	g = Graph()
	wfile = open(wordFile,'r')
	# create buckets of words that differ by one letter
	for line in wfile:
		word = line[:-1]
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]
	# add vertices and edges for words in the same bucket
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1,word2)
	return g

def rotateCheck(a1,a2):
	if len(a1) != len(a2):
		return False

	n = len(a1)
	if n == 0: return True

	j = 0
	for i in range(n):
		if a2[j] == a1[i]:
			j += 1
	# print("check2",a1[:n - j])
	# print("check3",a2[j:])
	return (j > 0 and a1[:n - j] == a2[j:] and a1[n - j:] == a2[:j])

print(rotateCheck([1,2,3,4,5],[3,4,5,1,2]))
print(rotateCheck([1,2,3,4,5],[5,1,2,3,4]))
print(rotateCheck([1,2,3,4,5],[1,2,3]))
