#avoid putting in class otherwise will not call function when printed

words = "words and stuff"

def reverse_word(words):

    length = len(words) #length of words
    s = length
    print("length",s)
    new_list = [None]*length # returns list of [None,None, ... length of words]

    for item in words:
        s = s - 1
        new_list[s] = item
    return new_list

print(reverse_word(words))

# Returns maximum profit with two transactions on a given
# list of stock prices price[0..n-1]
def maxProfit(price,n):

	# Create profit array and initialize it as 0
	profit = [0]*n

	# Get the maximum profit with only one transaction
	# allowed. After this loop, profit[i] contains maximum
	# profit from price[i..n-1] using at most one trans.
	max_price=price[n-1]

	for i in range( n-2, 0 ,-1):

		if price[i]> max_price:
			max_price = price[i]

		# we can get profit[i] by taking maximum of:
		# a) previous maximum, i.e., profit[i+1]
		# b) profit by buying at price[i] and selling at
		#    max_price
		profit[i] = max(profit[i+1], max_price - price[i])
		print("max loop",profit[i])

	# Get the maximum profit with two transactions allowed
	# After this loop, profit[n-1] contains the result
	min_price=price[0]

	for i in range(1,n):

		if price[i] < min_price:
			min_price = price[i]

		# Maximum profit is maximum of:
		# a) previous maximum, i.e., profit[i-1]
		# b) (Buy, Sell) at (min_price, A[i]) and add
		#    profit of other trans. stored in profit[i]
		profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
		print("min loop",profit[i])

	result = profit[n-1]

	return result

price = [2, 30, 15, 10, 8, 25, 80]
print("Maximum profit is", maxProfit(price, len(price)))

def lis(A):
	LIS = [1 for _ in range(len(A))]
	for i in range(len(A)):
		for j in range(i):
			if A[j] <= A[i]:
				LIS[i] = max(LIS[i], LIS[j] + 1)
	print("A",LIS)
	return max(LIS)

A = [12, 4, 54, 3, 23, 5, 23, 11, 23, 23, 3, 3, 4, 5 ,6] #3,5,11,23
print(lis(A))
print("LIS",lis(A))

arr = [0, 0, 1, 2, 0, 4, 0, 0 ,8 ,9]

def moveZero(arr):
	pos = 0
	for i in range(len(arr)):
		if arr[i] != 0:
			arr[pos] = arr[i]
			print("pos",arr[pos])
			pos += 1
			print("pos2",arr[pos])

	for i in reversed(range(pos, len(arr))):
		arr[i] = 0

print(moveZero(arr))
print("moveZero",arr)

# n = [1,2,5,8,11]
# k = 7
# def findPair(n,k):
# 	i = 0
# 	j = len(n)
#
# 	while(i < j):
# 		if n[i] + n[j] == k:
# 			return i,j
# 		elif n[i] + n[j] < k:
# 			i += 1
# 		elif n[i] + n[j] > k:
# 			j -= 1
#
# print('findPair',findPair(n,k))

# Dynamic Programming Python implementation of Coin
# Change problem
arr = [3,1,2,4]
m = len(arr)
n = 5

def count(S, m, n):

	# table[i] will be storing the number of solutions for
	# value i. We need n+1 rows as the table is constructed
	# in bottom up manner using the base case (n = 0)
	# Initialize all table values as 0
	table = [0 for k in range(n+1)]

	# Base case (If given value is 0)
	table[0] = 1

	# Pick all coins one by one and update the table[] values
	# after the index greater than or equal to the value of the
	# picked coin
	for i in range(0,m):
		print('i-----------',i)
		for j in range(S[i],n+1):
			print('S',S[i],'n',n)
			print('j',table[j])
			table[j] += table[j-S[i]]
			print('calculation',table[j-S[i]])
			# print('J',table[j])
			# print('Minus',S[i])
	return table[n]

# Driver program to test above function
x = count(arr, m, n)
print ('x',x)

lst = [1,2,3,4]
def solution(lst):

	# Start at index 2 (3rd element) and assign highest and lowest
	# based off of first two elements

	# Highest Number so far
	high = max(lst[0],lst[1]) #ex: 2

	# Lowest number so far
	low = min(lst[0],lst[1]) #ex: -5

	# Initiate Highest and lowest products of two numbers
	high_prod2 = lst[0]*lst[1] # -10
	low_prod2 = lst[0]*lst[1] # -10

	# Initiate highest product of 3 numbers
	high_prod3 = lst[0]*lst[1]*lst[2] # -950

	# Iterate through list
	for num in lst[2:]: #[30] btw 2 is included and then onward, lst[0] and lst[1] change as num moves up

		# Compare possible highest product of 3 numbers
		high_prod3 = max(high_prod3,num*high_prod2,num*low_prod2) #-950 for all
		print("high prod3",high_prod3)
		# Check for possible new highest products of 2 numbers
		high_prod2 = max(high_prod2,num*high,num*low) #-10,180,-475
		print("high prod2",high_prod2)
		# Check for possible new lowest products of 2 numbers
		low_prod2 = min(low_prod2,num*high,num*low)
		print("low prod2",low_prod2)
		# Check for new possible high
		high = max(high,num) #2 or ...95...
		print("high",high)
		# Check for new possible low
		low = min(low,num)#...-5... or 95
		print("low",low)
		#high and low are decided and this affects the high_prod's through each iteration
	return high_prod3

#solution is O(n) because it calculates the three highest products in one iteration
#space is O(1)
#if an algorithm involves finding the highest of anything it probably includes the max/min function
#solve in one iteration by using min and max
#Greedy approach becasue it must check every item and decide which is highest right then and there

print("lst",solution(lst))


def anagram(s1,s2):
	s1 = s1.replace(" ","")
	s2 = s2.replace(" ","")

	if len(s1) != len(s2):
		return False

	count = {}

	for letters in s1:
		if letters in count:
			count[letters] += 1
			print(count)
		else:
			count[letters] = 1

	for letters in s2:
		if letters in count:
			count[letters] -= 1
		else:
			count[letters] = 1

	for k in count:
		if count[k] != 0:
			return False

	return True

print("Anagram here:")
print(anagram("dog","god"))

#check if BST is valid - http://jelices.blogspot.com/2014/06/leetcode-python-validate-binary-search.html
class node:
	def __init__(self,val):
		self.value = val
		self.left = None
		self.right = None

	def isValidBST(self,root): #root is a node object
		return check_BST(root,float("-inf"),float("inf"))

	def check_BST(root,min,max):
		if root == None:
			return True

		if root.left <= root.value or root.value >= root.right:
			return False

		solution = check_BST(root.left,min,root.value)
		solution = solution and check_BST(root.right,root.value,max)


		return check_BST(root.left,min,root.value) and check_BST(root.right,root.value,max)


# def bubble_sort(arr):
#
#     swap_counter = 0
#     first = arr[0]
#     last = arr[-1]
#
#     for num in range(n):
#
#         for i in range(i,n):
#             swap_counter += 1
#             if arr[num] > arr[j]:
#                 arr[num], arr[j] = arr[j], arr[num]
#
#     if swap_counter == 0:
#         return 0
#
#     print('Array is sorted in',swap_counter,'swaps')
#     print('First Element:',first)
#     print('Last Element:',last)
#
# print(bubble_sort([1,3,2,4]))

#improved i guess
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps = 0
isSorted = False
aSize = len(a) - 1
while(not isSorted):
	isSorted = True
	for j in range(0, aSize):
		if a[j] > a[j+1]:
			temp = a[j]
			a[j] = a[j+1]
			a[j+1] = temp
			swaps += 1
			isSorted = False
	aSize -= 1

print("Array is sorted in "+str(swaps)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[-1]))

def two_sum(arr,targ):
	look_for = {}
	for n,x in enumerate(arr):
		try:
			print(arr)
			return look_for[x] + 1, n + 1
		except KeyError:
			look_for.setdefault(targ - x,n)
			print(look_for)

print(two_sum([2,4,5,6],9))

class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		#if odd then find middle number otherwise / between 2
		[list(a) for a in zip(nums1,nums2)]
		for i in a:
			if i == len(a) - 1:
				#print(i/2)
				return i / 2

nums1 = [1,2,3,4]
nums2 = [5,6,7,8]

print(findMedianSortedArrays(nums1,nums2))

nums = [1,1,2] #sorted array

def removeDuplicates(self, nums):

		if not nums:
			return 0

		newTail = 0

		for i in range(1, len(nums)): #important that i starts at index 1 not 0, must stay ahead, slow/fast runner
			if nums[i] != nums[newTail]: #checks if not equal otherwise moves to next item if they are equal
				newTail += 1 # moves array from index 0 to 1 then prepares for swap
				nums[newTail] = nums[i] #returns [1,2]

		return newTail + 1


print(removeDuplicates(nums))

item = 1000
def multipleOfThousand(self,item):
	sum = 0
	for i in range(1,item):
		if i % 3 == 0 or i % 5 == 0:
			sum += i

	return sum

print(multipleOfThousand(1000))
print(sum)

#Davids staircase - n power 3
def waysUpstairs(n):
	if (n < 1):
		return 0
	elif n == 0:
		return 1
	else:
		return waysUpstairs(n-1) + waysUpstairs(n-2) + waysUpstairs(n-3)

n = 100
print("Ways",waysUpstairs(n))
