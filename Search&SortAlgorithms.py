#merge sort
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid] # <-- mid
        righthalf = alist[mid:] # mid -->

        #recurses until it cant be split anymore
        mergeSort(lefthalf)
        mergeSort(righthalf)

        #after the splitting then resort to sorting
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1 #k increases after either if or else runs

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


#Binary Search
def binary_search(arr,item):
    #specify size
    first = 0
    last = len(arr) - 1

    found = False
    #while first is less than last and found is not true
    while first <= last and not found:

        mid = (first + last) // 2

        if arr[mid] == item:
            return True
        else:
            if item < arr[mid]:
                last = mid - 1 #sets up the new bounds for the next midpoint in while loop
            else:
                first = mid + 1

    return found

nums = [1,2,3,4,5,6,7,8,9]
item = 5
print(binary_search(nums,item))

#Recursive solution to binary search
def rec_binary_search(arr,ele):
    #NEVER FORGET YOUR BASE CASE
    if len(arr) == 0:
        return False

    else:
        mid = len(arr)//2

        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid],ele) #left half of array
            else:
                return rec_binary_search(arr[mid+1:],ele) #right half of array

print(rec_binary_search(nums,item))

#Hashing

#Sorting Algorithms - Bubble sort
#Largest item is continuously swapped to the right, if larger item is enocntered then swap and continue
def bubble(arr):
    #creates list backwards minus last element - [1,2,3,4,5] -> [4,3,2,1] minus last, in this case 5
    for n in range(len(arr)-1,0,-1):
        #print(list(range(len(arr)-1,0,-1)))
        #print(n)
        for k in range(n):
            #print('This is k',k)
            if arr[k] > arr[k+1]:
                tmp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = tmp
                print("arr",arr)

arr = [1,5,4,2,7]
bubble(arr)
print(arr)
#still bubble sort
arr = [5,4,3,1,6,8,10,9] # array not sorted
def b_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if(arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

b_sort(arr)
print("b sort:",arr)

#Selection sort - finds smallest element and sorts from bottom up
def selection_sort(arr):
    for fillslot in range(len(arr)-1,0,-1):
        #print("fillslot",fillslot)
        positionOfMax = 0

        for location in range(1,fillslot+1):
            #print("location",location) if location iterator is less than first element, swap
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp
        #print("fillslot",arr[fillslot])

selection_sort(arr)
print("selection:",arr)
#still selection sort - finds smallest element and sorts from bottom up
source = [4,2,1,10,5,3,100]
def sel_sort(source):
    for i in range(len(source)):
        mini = min(source[i:]) #find minimum element
        min_index = source[i:].index(mini) #find index of minimum element
        source[i + min_index] = source[i] #replace element at min_index with first element
        source[i] = mini                  #replace first element with min element
    #print(source)

#Insertion sort - makes sorted list in one pass, swaps along the way
#creates s sublist and next value is compared to values currently in sublist
def insertion_sort(arr):
    # n - 1 passes to sort, starts at 1
    #assume first element is already sorted
    for i in range(1,len(arr)):
        currentvalue = arr[i]
        position = i

        while position > 0 and arr[position-1] > currentvalue:
            arr[position] = arr[position-1]
            position = position-1 #A simple swap occurs here

        arr[position] = currentvalue

#Shell sort
def shell_sort(arr):

    sublistcount = len(arr)/2

    # While we still have sub lists
    while sublistcount > 0:
        for start in range(sublistcount):
            # Use a gap insertion
            gap_insertion_sort(arr,start,sublistcount)



        sublistcount = sublistcount / 2

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):

        currentvalue = arr[i]
        position = i

        # Using the Gap
        while position>=gap and arr[position-gap]>currentvalue:
            arr[position]=arr[position-gap]
            position = position-gap

        # Set current value
        arr[position]=currentvalue

new_arr = [1,11,14,5,8,9,10,3,21,4]
#Merge sort
def merge_sort(new_arr):

    if len(new_arr) > 1:
        mid = len(new_arr)/2
        lefthalf = new_arr[:mid] #before mid
        righthalf = new_arr[mid:] #after mid

        #Recursive call to sort lefthalf and righthalf - merge sort continuously breaks down list
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0 #tracker for left half
        j = 0 #tracker for right half
        k = 0 #tracker for final array, finished product

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]: #compares indexes of let and right half, the bigger gets added to arr and incremented
                new_arr[k] = lefthalf[i] #place back one at a time into original list

                i += 1

            else:
                new_arr[k] = righthalf[j]
                j += 1

            k += 1

        while i < len(lefthalf):
            new_arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            new_arr[k] = righthalf[j]
            j += 1
            k += 1


#merge_sort(arr)
print("Merging print",new_arr)

#Quicksort
def quick_sort(arr):
    quick_sort_help(arr,0,len(arr)-1)

def quick_sort_help(arr,first,last):

    if first < last:
        splitpoint = partition(arr,first,last)

        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)

def partition(arr,first,last):

    pivotvalue = arr[first] #start by selecting pivot value

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue: #pivot value is first item, checks against it
            leftmark += 1
            #print('leftmark',arr[leftmark])

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
            #print('rightmark',arr[rightmark])

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

arr = [1,3,6,23,11,12,16,9,10]
quick_sort(arr)
print('quick:',arr)

lst = [-5,2,95,30,12,7,-21,45,23]
def solution(lst):

    # Start at index 2 (3rd element) and assign highest and lowest
    # based off of first two elements

    # Highest Number so far
    high = max(lst[0],lst[1])

    # Lowest number so far
    low = min(lst[0],lst[1])

    # Initiate Highest and lowest products of two numbers
    high_prod2 = lst[0]*lst[1]
    low_prod2 = lst[0]*lst[1]

    # Initiate highest product of 3 numbers
    high_prod3 = lst[0]*lst[1]*lst[2]

    # Iterate through list
    for num in lst[2:]:

        # Compare possible highest product of 3 numbers
        high_prod3 = max(high_prod3,num*high_prod2,num*low_prod2)

        # Check for possible new highest products of 2 numbers
        high_prod2 = max(high_prod2,num*high,num*low)

        # Check for possible new lowest products of 2 numbers
        low_prod2 = min(low_prod2,num*high,num*low)

        # Check for new possible high
        high = max(high,num)

        # Check for new possible low
        low = min(low,num)

    return high_prod3

#solution is O(n) because it calculates the three highest products in one iteration
#space is O(1)
#if an algorithm involves finding the highest of anything it probably includes the max/min function
#solve in one iteration by using min and max
#Greedy approach becasue it must check every item and decide which is highest right then and there

print("lst",solution(lst))
