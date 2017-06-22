# The graph will be directed and the edges can hold weights.
# We will have three classes, a State class, a Node class, and finally the Graph class.
# We're going to be taking advantage of two built-in tools here, OrderDict and Enum

from enum import Enum

class State(Enum):
    unvisited = 1 #White
    visited = 2 #Black
    visiting = 3 #Gray

# Now for the Node class we will take advantage of the OrderedDict object
# in case we want to keep trak of the order keys are added to the dictionary.
#http://www.python-course.eu/graphs_python.php

from collections import OrderedDict

class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node, val = weight

    def __str__(self):
        return str(self.num)

class Graph:

    def __init__(self):
        self.nodes = OrderedDict()  # key = node id, val = node

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node # nodes[num] sets the key = node id, val = node
        #The above code adds a value to key in dictionary, key "num" with value node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight



g = Graph()
g.add_edge(0, 1, 5)

g.nodes

#Knight's tour - DFS
#Just a note, but if function recurses itself and it is meant to do DFS, just picture it searching nodes even deeper


#DFS Implementation
graph = {'A': set(['B', 'C']), #used in example below
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#One version
def dfs(graph, start):
    visited, stack = set(), [start] #1 - set because node cant be visited twice, and must have initial value in stack
    while stack: #2 - while stack is full, remeber initial value in stack
        vertex = stack.pop()
        if vertex not in visited: #3
            visited.add(vertex)
            stack.extend(graph[vertex] - visited) #Ex: set(['B', 'C']) - set('B') -> {'C'}, eventually returns the visited nodes
    #print('visited',visited)
    return visited

print(dfs(graph, 'A'))

#another version of DFS - remeber DFS uses a stack, BFS a Queue
def depthFirst(startingNode, soughtValue):
   visitedNodes = set() #set only allows uniques
   stack = [startingNode] #first item in stack is starting node

   while len(stack) > 0:
      node = stack.pop() #pop the first node, in this case starting node
      if node in visitedNodes: #continue to next iteration if node is in the set()
         continue

      visitedNodes.add(node) #add node to the set()
      if node.value == soughtValue: #checks to make sure we haven't reached the soughtValue(the end)
         return True #This is the end goal and if htere is an end point this will return, otherwise false

      for n in node.adjacentNodes: #Checks the neighbors, if not in the set, add them to set
         if n not in visitedNodes:
            stack.append(n)
   return False

#BFS Implementation
from collections import deque # Remember a deque operates in 0(1) and allows addition and removals from both ends

def breadthFirst(startingNode, soughtValue):
   visitedNodes = set()
   queue = deque([startingNode])

   while len(queue) > 0:
      node = queue.pop()
      if node in visitedNodes:
         continue

      visitedNodes.add(node)
      if node.value == soughtValue:
         return True

      for n in node.adj:
         if n not in visitedNodes:
            queue.appendleft(n)
   return False
