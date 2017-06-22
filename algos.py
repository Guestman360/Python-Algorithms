import sys
#from pythonds.basic.stack import Stack

#Algo for search engine company - can use set or dictionary
def twoSum(lst,target):

	seen = set()

	for num in lst:

		num2 = target - num # 11 - 1, 11 - 2, 11 - 4 etc...

		if num2 in seen: #If sum can be found program will end here
			return True #Looks for 10,9,7 - stops and returns true becasue 7 is in lst

		seen.add(num) #will just keep adding until found
					  #{1,2,4}

	return False

lst = [1,2,4,7,8,9]
target = 11
print(twoSum(lst,target))

def findUnique(arr):
	result = 0
	for num in arr:
		result ^= num #Uses XOR
		#print("result",result)

	return result

def findUnique2(arr2):
#https://stackoverflow.com/questions/1089987/given-an-array-of-numbers-except-for-one-number-all-the-others-occur-twice-gi?noredirect=1&lq=1
	hash = {} # Second solution makes use of hash, o(n) time & space

	for num in arr2:
	   if not num in hash:
		   hash[num] = 1
	   else:
		   del hash[num]

	for key in hash:
		print("Key",key) #unique number returned here, print whatevers left in hash

arr = [1,2,3,2,1]
arr2 = [1,4,6,4,1]
print(findUnique(arr))
print(findUnique2(arr2))

#kjfbshdbv
def priceSort(unsorted_prices,max_price):
#imagine creating an array of 0's the size proportional to max price, number is put in its order
#example 12 is put in 12th 0 place, then just enumerate over and put into another array
	# list of 0s at indices 0 to max_price
	prices_to_counts = [0]* (max_price+1)

	# populate prices
	for price in unsorted_prices:
		print("prices_to_counts",prices_to_counts)
		prices_to_counts[price] +=1 #just adds a 1 to that index

	# populate final sorted prices
	sorted_prices = []

	# For each price in prices_to_counts
	for price,count in enumerate(prices_to_counts):
		# print("price",price)
		# print("count",count)
		# for the number of times the element occurs
		for time in range(count):
			#print("price goind in", price)
			# add it to the sorted price list
			print(sorted_prices)
			sorted_prices.append(price)

	return sorted_prices

unsorted_prices = [12,19,13,25,25,39,30,50,32]
max_price = 50
print(priceSort(unsorted_prices,max_price))

#Stock algorithm
def profit2(stock_prices):

	# Check length
	if len(stock_prices) < 2:
		raise Exception('Need at least two stock prices!')

	# Start minimum price marker at first price
	min_stock_price = stock_prices[0]

	# Start off with an initial max profit
	max_profit = stock_prices[1] - stock_prices[0]

	# Skip first index of 0
	for price in stock_prices[1:]:


		# NOTE THE REORDERING HERE DUE TO THE NEGATIVE PROFIT TRACKING

		# Check the current price against our minimum for a profit
		# comparison against the max_profit
		comparison_profit = price - min_stock_price
		print("comparison",comparison_profit)
		# Compare against our max_profit so far
		max_profit = max(max_profit,comparison_profit)
		print("max",max_profit)
		# Check to set the lowest stock price so far
		min_stock_price = min(min_stock_price,price)
		print("min",min_stock_price)

stock_prices = [100,50,75,160,20,300,250] # imagine going through lsit and comapring keeping the max as it goes along
print(profit2(stock_prices))

#launchcode questions
numbers = [12,13,15,100,50,32,30,34]
# def  closestNumbers(numbers):
	# numbers = sorted(numbers)
	#     pairs = []
	#     current_min = float("inf")
	#     for i in range(1,len(numbers)):
	#         diff = numbers[i] - numbers[i-1]
	#         if(numbers[i] - numbers[i-1] == current_min):
	#             pairs.append((numbers[i-1],numbers[i]))
	#         elif(diff < current_min):
	#             pairs = []
	#             current_min = numbers[i] - numbers[i-1]
	#             pairs.append((numbers[i-1],numbers[i]))
	#     return pairs

# def  closestNumbers(numbers):
# 	nums = numbers.sort()
# 	diff = nums[1]-nums[0]
# 	pairs = [nums[0],nums[1]]
# 	for i in range(1,len(nums)-1):
# 		if nums[i+1]-nums[i] < diff:
# 			pairs = []
# 			pairs.append(nums[i])
# 			pairs.append(nums[i+1])
# 			diff = abs(nums[i+1]-nums[i])
# 		elif nums[i+1]-nums[i] == diff:
# 			pairs.append(nums[i])
# 			pairs.append(nums[i+1])
#
# 	print(pairs)

#Correct solution
def  closestNumbers(numbers):

	list = sorted(numbers)
	mindiff = float('inf')
	result = ''

	for i in range(len(list) - 1):
		diff = abs(list[i] - list[i + 1])
		if diff > mindiff:
			continue
		elif diff < mindiff:
			mindiff = diff
			result = ''
		print("result",str(result))
		result += str(min(list[i], list[i + 1])) + " " + str(max(list[i], list[i + 1])) + "\n"

unsorted = [5,2,7,8,-2,25,25]

def  meanderingArray(unsorted):
	arr = sorted(unsorted)
	low = 0
	high = len(arr)-1
	newArr = []

	for i in arr:

		if arr[high] < arr[low]:
			#del newArr[high]
			return newArr

		newArr.append(arr[high])
		newArr.append(arr[low])
		high -= 1
		low += 1

	print(newArr)

print(meanderingArray(unsorted))

class Stack:
	def __init__(self):
		self.items = []

	def pop(self):
		if self.isEmpty():
			raise RuntimeError("Attempt to pop an empty stack")
		topIdx = len(self.items)-1
		item = self.items[topIdx]
		del self.items[topIdx]
		return item

	def push(self,item):
		self.items.append(item)

	def top(self):
		if self.isEmpty():
			raise RuntimeError("Attempt to get top of empty stack")
		topIdx = len(self.items)-1
		return self.items[topIdx]
	def isEmpty(self):
		return len(self.items) == 0

#Parenthesis Checker
def parCheck(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

print(parCheck("((()))"))
print(parCheck("((())"))
