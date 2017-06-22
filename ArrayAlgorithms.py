#Array Algorithms
import random
import collections

def finder(arr):
    random.shuffle(arr)

    for x in arr:

        while arr:
            x = arr.pop()

            return(x,arr)

print(finder([1,2,3,4,5,6]))
#another solution
def find(arr1,arr2):
    #sort arrays
    arr1.sort()
    arr2.sort()

    #compare elements in sorted arrays - zip([1,2,3],[4,5,6]) -> [(1,4), (2,5), (3,6)]
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

print(find([3,2,5,4,1],[1,5,4,2]))
#linear solution
def finder2(arr1,arr2):
    #import default dicitonary
    d = collections.defaultdict(int)
    #count number of times each element shows up in arr2
    for num in arr2:
        d[num] += 1
    #check if num in arr1 is 0, this means it is odd one out and return that
    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1


print(finder2([3,2,5,4,1],[1,5,4,2]))
#last one - linear space and time complexity, done with "XOR" exclusive or
def finder3(arr1,arr2):
    result = 0

    #perform an XOR between the numbers in the arrays
    for num in arr1+arr2:#arr1+arr2 -> [3,2,5,4,1,1,5,4,2] just puts arrays end to end
        result^=num
        print(result)

    return result

print("Result:")
print(finder3([3,2,5,4,1],[1,5,4,2]))

#Important interview question, study up -
def large_cont_sum(arr):

    if len(arr) == 0:
        return 0
    #var max_sum and current_sum are set to first element
    max_sum = current_sum = arr[0]
    #iterate through arr but exclude the first since both are set to arr[0]
    for num in arr[1:]:
        # Start the max and current sum at the first element
        #currentsum plus num were at right now vs. the given number
        #max is a method, find the greater of the two
        current_sum = max(current_sum+num,num)
        print("current_sum",current_sum)
        max_sum = max(current_sum,max_sum)
        print("max_sum",max_sum)
    return max_sum

print("large cont sum:")
print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1])) #negative numbers ignored essentially

#reverse words algorithms, multiple
def rev_words1(s):
    return " ".join(reversed(s.split()))
#Or
def rev_words2(s):
    return " ".join(s.split()[::-1])

#Custom function for rev_words3 ----------------------------------------------
def reverse_word(words):

    length = len(words) #length of words
    s = length
    print("length",s)
    new_list = [None]*length # returns list of [None,None, ... length of words]

    for item in words:
        s = s - 1
        new_list[s] = item
    return new_list

#Offical one, do this in interview
def rev_words3(s):

    words = []
    length = len(s)
    spaces = [' '] #list with a white space as first element

    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i

            while i < length and s[i] not in spaces:
                print(i)
                i += 1

            words.append(s[word_start:i])
            print("words",words)
        i += 1

    #return " ".join(reversed(words))
    return reverse_word(words)

print(rev_words3("money get bitches fuck"))

#string compression
def compress(s):
    #"run length compression algorithm"
    #begin run as empty string
    r = ""
    l = len(s)
    #chekc for length 0
    if l == 0:
        return ""
    #check for length 1
    if l == 1:
        return s+"1"

    #initializing values
    last = s[0]
    cnt = 1
    i = 1

    while i < l:
        #check to see if same letter - AAAAA then goes to else and creates A5
        #repeats for B - BBBB then creats A5B4 ... and so on
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            print(r) #A5B4C4
            cnt = 1

        # Add to index count to terminate while loop
        i += 1
    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r

print(compress('AAAAABBBBCCCC'))

#unique characters in string
def uniq_str(s):
    #print("Set",set(s)) - has built in data structure and function
    #This works becasue everything in set is already unique by default so it is checking that
    #both stirngs match in length
    return len(set(s)) == len(s)
print(uniq_str("fuck"))

def uniq_str2(s):

    chars = set()

    for let in s:
        #if string is entirely unique then only the else statement runs
        #otherwise if a dupicate character is encountered the if statement runs
        if let in chars:
            return False
        else:
            chars.add(let)

    return True

print(uniq_str2("fuck you"))
