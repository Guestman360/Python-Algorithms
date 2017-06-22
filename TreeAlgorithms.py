#Tree Algorithms
#https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/tree/master/Recursion/Recursion%20Interview%20Problems/Recursion%20Problems%20-%20%20SOLUTIONS
#https://jeremykun.com/2012/01/12/a-spoonful-of-python/
#http://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do
#Represent a tree with a list in Python
def BinaryTree(r):
    return[r,[],[]]

def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        #visual representation -         t
        #                    newBranch          []
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root

def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])

    return root

def getRootVal(root):
    #Just returns the value of root node
    return root[0]

def setRootVal(root,newVal):
    #resets the value of root node
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
print(r)


class BinaryTree(object):

    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):

        if self.leftChild == None:
            #if leftchild has no node then add a node to tree
            self.leftChild = BinaryTree(newNode)
        else:
            #insert leftchild node and push existing child down one level of existing tree
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):

        if self.rightChild == None:

            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    #Four methods to access values of tree
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

rt = BinaryTree('a')
rt.getRootVal()
rt.insertLeft('b')
rt.getLeftChild().getRootVal()
print(rt)

#pre order tree - a method uses (self, parameter) a function just uses parameter no self
def preorder(tree):
    #base case - check if tree exists, if not takes no action
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

'''
preorder
        1
    2       3
'''

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

'''
postorder
        3
    1       2
'''

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

'''
inorder
        2
    1       3
'''

# class node:
#     def __init__(self,val):
#         self.value = val
#         self.left = None
#         self.right = None
#
#     def isValidBST(self,root): #root is a node object
#         return check_BST(root,float("-inf"),float("inf"))
#
#     def check_BST(root,min,max):
#         if root == None:
#             return True
#
#         if root.left <= root.value or root.value >= root.right:
#             return False
#
#         solution = check_BST(root.left,min,root.value)
#         solution = solution and check_BST(root.right,root.value,max)
#
#
#         return check_BST(root.left,min,root.value) and check_BST(root.right,root.value,max)


#Binary Heap Implementation
class BinHeap(object):

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i): # example set i to 6, index 6
        while i // 2 > 0: #[1,2,3,4,5,6] -> index 6 // 2 = 3 its parent node, in this case 3
            if self.heapList[i] < self.heapList[i // 2]: #if 6 is less than 3
                tmp = self.heapList[i // 2] #tmp = index 3
                self.heapList[i // 2] = self.heapList[i] # 3 = 6
                self.heapList[i] = tmp # 6 = 3
            i = i // 2

    def insert(self,k):
        self.heapList.append(k) #add to heap, at the end
        self.currentSize = self.currentSize + 1 #must accomodate new node so currentSize add 1
        self.percUp(self.currentSize) #let percUp function do heavy lifting

    def percDown(self,i):
        while(i * 2) <= self.currentSize: #take the parameter i and * 2, check if smaller than the size of heap
            mc = self.minChild(i) # set to minChild
            if self.heapList[i] > self.heapList[mc]: #if index is greater than index minChild
                tmp = self.heapList[i] #if so then set tmp to that index
                self.heapList[i] = self.heapList[mc] #that index now equals minChild
                self.heapList[mc] = tmp #That minChild now equas tmp, or the original index compared to
            i = mc

    def minChild(self):
        if i * 2 + 1 > self.currentSize: #ex: if 3 * 2 + 1 = 7 > currentSize
            return i * 2 # return 6, think in therms of a tree, left leaf of node
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]: #compares the left leaf node with the right leaf node
                return i * 2 # return left leaf node
            else:
                return i * 2 + 1 # otherwise return right left node

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize] # is equal to current size of heap
        self.currentSize = self.currentSize - 1 #reduce currentSize by 1 because of pop mehtod below
        self.heapList.pop() #pops off last item, remember can be represented by array
        self.percDown(1)
        return retval
#http://stackoverflow.com/questions/6167238/what-does-mean
    def buildHeap(self,alist):
        i = len(alist) // 2 #find middle node
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:] #alist[:] returns a shallow copy
        while (i > 0): #while loop builds by percolating down to create heap
            self.percDown(i)
            i = i - 1

#Binary Search Tree Implementation - BST
class TreeNode:

    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:

                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):

        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):

        if self.size > 1:

            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):

        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():

                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():

                if self.isLeftChild():

                    self.parent.leftChild = self.leftChild
                else:

                    self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
        else:

            if self.isLeftChild():

                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):

        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:

                if self.isLeftChild():

                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
#loops to find the farthest left chile i.e. the smallest
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self,currentNode):

        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior

            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:

                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
            else:

                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

#VARIFYING A BST
#node.leftChild <= value <= node.rightChild, smaller numbers on left and greater on right of root node value

class Node:
    def __init__(self,k,val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None

    def tree_max(node):
        if not node:
            return float("-inf")
        max_left = tree_max(node.left) #recursive call
        max_right = tree_max(node.right)
        return max(node.key,max_left,max_right)

    def tree_min(node):
        if not node:
            return float("-inf")
        min_left = tree_min(node.left) #recursive call
        min_right = tree_min(node.right)
        return max(node.key,min_left,min_right)

    def verify(tree_vals):
        if not node:
            return True
        if (tree_max(node.left) <= node.key <= tree_min(node.right) and verify(node.left) and verify(node.right)):
            return True
        else:
            return False

root = Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

#print(verify(root))


#or search tree in order
tree_vals = []

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild)
        tree_vals.append(tree.getRootVal)
        inorder(tree.getRightChild)

def sort_check(tree_vals): #checks if values appended to tree_vals are equal to a sorted tree_vals
    return tree_vals == sorted(tree_vals)

#Trim BST Algorithm
def trimBST(tree,minVal,maxVal):
    #minVal and maxVal - example 5 and 20, BST will only accept numbers between these two
    if not tree:
        return

    tree.left = trimBST(tree.left,minVal,maxVal) #recursion traverses tree checking
    tree.right = trimBST(tree.right,minVal,maxVal)

    if minVal <= tree.val <= maxVal: # Just returns tree, this is good, checks if it folows BST rules
        return tree

    if tree.left < minVal: # if tree.left is less than stated minVal then return right becasue we know they are too small
        return tree.right #if less than 5 then just get rid of those nodes

    if tree.right > maxVal: # if maxVal is 20 for example then anything over right is too big so just return left
        return tree.left #if greater than 20 then get rid of those nodes

# t = BinarySearchTree(6)
# t.put(15)
# t.put(8)
# t.put(25)
# t.put(29)
# t.put(17)
# t.put(12)
# t.put(14)
# t.put(5)
# t.put(10)
#
# print(trimBST(t,10,20))

# Python program to check if a binary tree is bst or not - VERIFY BST

INT_MAX = 4294967296
INT_MIN = -4294967296

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTRec(root, float("-infinity"), float("infinity"))

    def isValidBSTRec(self, root, min, max):
        if root == None:
            return True
        if root.val<=min or root.val>=max:
            return False
        solution = self.isValidBSTRec(root.left, min, root.val)
        solution = solution and self.isValidBSTRec(root.right, root.val, max)
        return solution

# ------------------------------------------------------- Alternative

# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))

# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, maxi))

# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root)):
    print("Is BST")
else:
    print("Not a BST")
