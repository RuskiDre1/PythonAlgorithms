# CS 350: Homework 2
# Due: Week of 4/11
# Name: Andrey Toderyan



#########################################3
# Problem 1:
#
# Find a pair with a given sum.
#
# input: a list of integers l, an integer s
# return None if this sum doesn't exist in the array.
# output: a pair of numbers (a,b) where a,b are in l, and a + b == s
# findSum([1,3,5], 8) returns (3, 5)
# 
# What data structure did you use? none, but I should have
# Running Time: 0(n^2)
#########################################3

def findSum(l, s):
    """
    >>> findSum([1,3,5], 8)
    (3, 5)
    >>> findSum([1,2,5], 8)
    None
    """

   
    #print(len(l))
    for i in range(len(l)):
        for j in range(len(l)):
            if(l[i] != l[j] and l[i] + l[j] == s):
                return (l[i],l[j])
    
    print(None)
    return None
    

# #########################################3
# # Problem 2:
# #
# # Find the mode of a list of numbers.
# # The mode of a list is the most commonly occurring number in the list.
# #
# # input: a list of integers l
# # output: the mode of l.
# # mode([1,2,3,3,4,5]) returns 3
# # 
# # What data structure did you use? dictionary
# # Running Time: 
# #########################################3

def mode(l):
    """
    >>> mode([1,2,3,3,4,5])
    3
    """
    freq = {}
    
    for i in l:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for key, value in freq.items():
        if value == max(freq.values()):
            return key

pass

# print( mode([1,2,3,3,4,5]) )

#########################################3
# Problem 3:
#
# We talked about a ring buffer in class
# A ring buffer has four methods
# pushFront(x)
# pushBack(x)
# popFront()
# popBack()
#
# Your job is to implement these four methods.
# We can't just use the list append method to resize the ring buffer.
# we might have front and back in the middle of the buffer,
# and append only adds new space at the end.
# for that reason, you're going to have to copy
# the array over to a bigger one manually.
#
# I've provided a malloc function to allocate a new array.
# You need to copy the old array into the new one
# but be sure to keep elements in the correct position
#
# For example if we have the buffer :
#
#     v back
# [3, 4, 1, 2]
#        ^ front
#
# and we were to resize it, then the new buffer should be
#     v back
# [3, 4, None, None, None, None, 1, 2]
#                                ^ front
#    
# pushFront Running Time:  0(1)
# pushBack Running Time:  0(1)
# popFront Running Time: 0(1)
# popBack Running Time: O(1)
#########################################3

def malloc(size):
    return [None] * size

class RingBuffer():
    """
    >>> r = RingBuffer()
    >>> r.pushBack(3)
    >>> r.pushBack(4)
    >>> r.pushBack(5)
    >>> r.pushFront(2)
    >>> r.pushFront(1)
    >>> r.popFront()
    1
    >>> r.popFront()
    2
    >>> r.popFront()
    3
    >>> r.popFront()
    4
    >>> r.popFront()
    5
    """

    def __init__(self):
        self.size = 0
        self.body = []
        self.front = 0
        self.back = 0

    # This method isn't mandatory,
    # but I suggest you implement it anyway.
    # It will help to test this method on it's own.
    # Think carefully about what cases you can have with front and back.
    def resize(self):
        if(self.size == 0):
            self.body = [None] * 4
            self.size = 4
            return self
        
        #else copy over to larger and set point to that
        self.size = self.size * 2
        new_array = [None] * self.size

        #copy from back to edge
        x = 0
        while x < self.back:
            new_array[x] = self.body[x]
            x+=1
        #copy from front to edge
        x = self.front
        while x < 0:
            new_array[x] = self.body[x]
            x+=1

        self.body = new_array

        return self 

        pass
    def pushFront(self, x):
        if(-self.front + self.back >= self.size):
            self.resize()

        self.front -= 1
        self.body[self.front] = x

        pass

    def print_all(self):
        x = 0 
        while x < self.size:
            print(self.body[x])
            x += 1


    def pushBack(self, x):
        if(-self.front + self.back >= self.size):
            self.resize()
        
        self.body[self.back] = x
        self.back += 1

        pass

    def popFront(self):
        print(self.body[self.front])
        self.body[self.front] = None
        self.front += 1

        pass
    def popBack(self):
        print(self.body[self.back])
        self.back -= 1

        pass

# r = RingBuffer()
# r.pushBack(3)
# r.pushBack(4)
# r.pushBack(5)
# r.pushFront(1)
# r.popFront()
#     #1
# r.popFront()
#     #2
# r.popFront()
#     #3
# r.popFront()
#     #4
# r.popFront()
#    # 5




#########################################3
# Problem 4:
#
# We talked about a Heap_body in class
# A Heap_body is a data structure that has a constructor,
# a push method, and a pop method.
# Your job is to implement these methods in Python.
# I've given you the skeleton for the class,
# you need to fill it in.
# 
# 
# push Running Time: O(log n)
# pop Running Time: O(log n)
#########################################3
import sys
class Heap_class():
    """
    >>> h = Heap_class()
    >>> h.push(3)
    >>> h.push(2)
    >>> h.push(4)
    >>> h.push(1)
    >>> h.push(5)
    >>> h.pop()
    1
    >>> h.pop()
    2
    >>> h.pop()
    3
    >>> h.pop()
    4
    >>> h.pop()
    5
    """

    def __init__(self):
        self.maxsize = 15
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
 
    # Function to heap the node at pos
    def minHeapify(self, pos):
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):
 
                # Swap with the left child and heap
                # the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.switch(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
 
                # Swap with the right child and heap
                # the right child
                else:
                    self.switch(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
 
    # Function to insert a node into the heap
    def push(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
 
        current = self.size
 
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.switch(current, self.parent(current))
            current = self.parent(current)

    def pop(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped
 
    # Function to print the contents of the heap
    # def Print(self):
    #     for i in range(self.size+1):
    #         print(self.Heap[i])

    #helper functions
    def parent(self, pos):
        return pos//2
    def leftChild(self, pos):
        return 2 * pos
    def rightChild(self, pos):
        return (2 * pos) + 1
    def isLeaf(self, pos):
        return pos*2 > self.size
    def switch(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
     
 
    # Function to build the min heap using
    # the minHeapify() function
    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
    
    

# h = Heap_class()
# h.push(3)
# h.push(2)
# h.push(4)
# h.push(1)
# h.push(5)

# h.pop()
#     #1
# h.pop()
#     #2

# h.pop()
#     #3
# h.pop()
#     #4
# h.pop()
#     #5


if __name__ == "__main__":
    import doctest
    doctest.testmod()
