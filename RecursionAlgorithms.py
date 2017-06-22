#from future import division

# Dynamic Programming Python implementation of Coin
# Change problem
arr = [1, 2, 3]
m = len(arr)
n = 4

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
		print(i)
		for j in range(S[i],n+1):
			table[j] += table[j-S[i]]
			print(table[j])
	return table[n]

# Driver program to test above function
x = count(arr, m, n)
print (x)


n = 1234
print(str(n)[::-1]) #quick way to reverse number or string - :: means whole list

#Factorial recursion practice
def fact(n):

	#start off with a base case
	if n == 0:
		return 1

	else: #where recursion takes place
		return n * fact(n-1)

print(fact(10))

def zero_sum(n):

	if n == 1:
		return 1

	else:
		return n + zero_sum(n-1)

print(zero_sum(4))

def sum_func(n):
# checks if length of numbers is one, converts integers to string to check this
	if len(str(n)) == 1:
		return n

	else:
		return n%10 + sum_func(n//10) # // is classic division for python 3, must pay attention
		#4321%10 = 1 + 4321/10(432.1) -> 432 because // means floor division
print("sum func",sum_func(4321))

#very python-y solution
def word_split(phrase, list_of_words, output = None):
	#Base case
	if output is None:
		output = [] #set as list here otherwise will overwrite list created recursively in argument

	for word in list_of_words:
		#if phrase starts with the word then we have a splitpoint
		if phrase.startswith(word):
			#append word in output list
			output.append(word)
			#recursion occurs here
			return word_split(phrase[len(word):], list_of_words, output)

	return output

print(word_split('dogisgod', ['god','is','dog']))

#Memoization read article on

#Announce to interviewer that you need a base case and a recursive case
def reverse(s):
	#Base case
	if len(s) <= 1:
		return s
	#recursive case - [1:] means 'all but the first'
	return reverse(s[1:]) + s[0] #plus the first letter
	#grab first element of string s[0] then tack it onto recursive call
	#s[1:] in 'abc' means 'bc' + 'a' ---> 'bca'
print(reverse('fuck you'))

#String Permutation
def permute(s):
	#To put the finished result
	out = []
	#Base case
	if len(s) == 1:
		out = [s]
	#start by taking off first letter, in case of 'abc' take a and find perm for b&c
	else:
		#for every letter in string, i = index in string and let = letter in enumerate
		#this handles the first letter a and takes away from abc, leaving bc to permute
		for i,let in enumerate(s):
			#Recursive call - s[:i] means everything up to current index 'i'
			#s[i+1:] means everyting index + 1 to the end
			for perm in permute(s[:i] + s[i+1:]):
				#print(permute(s[:i] + s[i+1:]))
				#print('let is', let)
				#print('perm is', perm)
				#add it to the output
				out += [let+perm] #when a is done adds a + cb, a + bc to out, then oves to b and c
				#print('out',out)
	return out

print(permute('abc'))

#Fibonacci sequence
#Recursive option - print to te nth number fibonacci
def fib_rec(n):

	if n == 0 or n == 1:
		return n

	else:
		return fib_rec(n - 1) + fib_rec(n - 2)

print(fib_rec(10))

#Dynamic programming option(Memoization) store previous known results in memory

#Cache
n = 10 #must know n beforehand in this method
cache = [None] * (n+1)

def fib_dyn(n):

	#Base case
	if n == 0 or n == 1:
		return n
	#Check Cache
	if cache[n] != None:
		return cache[n]

	#Keep Setting Cache / Recursive
	cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

	return cache[n]

print("fib_dyn",fib_dyn(10))

#Iterative option
def fib_iter(n):
	#Set a starting point
	a,b = 0,1

	for i in range(n):
		#This is called tuple unpacking, pythonic solution saves me from using temp
		a,b = b, a + b
		#0,1 = 1, 0+1, so a = 1 and b = 1 -> 1,1 = 1, 1+1 so a = 1 and b = 2
		#1,2 = 2, 1+2 -> so a = 2 and b = 3 ...and so on...
	return a


print(fib_iter(10))

def rec_coin(target,coins):
	#default value set to target
	min_coins = target
	#checks to see if target is in coin values list
	if target in coins:
		return 1

	else:
		#For every coin value in coin list that is <= target recurse and count coin and subtract from target
		#This is called list comprehension
		for i in [c for c in coins if c <= target]:#creates a new list

			#Add a coin count + to recursive call, sub value of coin from target
			num_coins = 1 + rec_coin(target-i,coins)
			#Reset min here if the new num_coins is < min_coins
			if num_coins < min_coins:

				min_coins = num_coins

	return min_coins

print(rec_coin(15,[1,5,10]))
#rec_coin is the inneficient way to do this becasue we recalcuate values we
#already solved, this is one of the shortcomings of recursion as it can lead to
#slow run times becasue computer is busy recalculatiing
#A solution is dynamic programming / Memoization

#Dynamic solution to coin problem
#known_results is a cache and third parameter
def rec_coin_dynam(target,coins,known_results):

	#Default output to target
	min_coins = target

	#Base Case - if target is in coins then known_results at target = 1
	if target in coins:
		known_results[target] = 1
		return 1
	#return a known result if it happens to be greater than 1
	elif known_results[target] > 0:
		return known_results[target]

	else:
		#for every coin value that is <= target
		for i in [c for c in coins if c <= target]:
			#target - i increments the current target value, if found 5 then 10 - 5 then recurses
			num_coins = 1 + rec_coin_dynam(target - i,coins,known_results)
			#print('num_coins:',num_coins)
			if num_coins < min_coins:

				min_coins = num_coins

				#reset that known result
				known_results[target] = min_coins

	return min_coins

#When dealing with dynamic/memoization make sure to declare parameter val beforehand
target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)
print('min coins:', rec_coin_dynam(target,coins,known_results))

arr_num = [1,2,3,4,5]
'''
def reverse_array(arr,start,end):
	if start >= end:
		return
	temp = arr[end]
	arr[end] = arr[start]
	arr[start] = temp
	return reverse_array(arr,start+1,end-1)

print(reverse_array([1,2,3,4],arr_num[0],len(arr_num)-1))
'''
#Tower of Hanoi
# def towerOfHanoi(n,beg,tmp,end):
#
#     if n == 1:
#         return print("Number of moves %d" % len(end))
#
#     else:
#         towerOfHanoi(n-1,beg,end,tmp)
#         towerOfHanoi(1,beg,tmp,end)
#         towerOfHanoi(n-1,tmp,beg,end)
#
#
# stack1 = [5,4,3,2,1]
# stack2 = []
# stack3 = []
# print(towerOfHanoi(len(stack1),stack1,stack2,stack3))
