
# CS 350: Homework 3
# Due: Week of 4/18
# Name: Andrey Toderyan 

# for this homework, unless I'm asking you to sort a list,
# you are allowed to use the sorted function in Python.
# sorted takes a list, and returns a sorted copy of the list in Theta(n*log(n)) time.

############################################################################
#
# Problem 1
# Compute the largest gap between two numbers in a list.
#
# for example: gap([1,6,2,4,9]) == 3 because the gap between 6 and 9 is 3.
# The gap isn't 8 because even thought 9-1 is 8, there is a 4 in the middle
# of those numbers.
############################################################################
def gap(l):
    """
    >>> gap([1,6,2,4,9])
    3
    """
    l.sort()
    max_d = 0

    for i in range(len(l)):
        j = i+1
        if(j == len(l)):
            break
        gap = l[j] - l[i]
        if( gap > max_d):
            max_d = gap
           
     
    return max_d

    pass

############################################################################
#
# Problem 2
# We can concatenate two numbers together to get a new number.
# for example: 44 concatenated with 55 = 4455
# We can concatenate a list of numbers by concatenating all the numbers.
# concat([1,2,55,3]) = 12553
#
# If we rearrange the list, we can get a different number.
# concat([2,55,1,3]) = 25513
#
# Write a function to find the largest value we can get from concatenating a list.
#
# Running Time: O(n^2)
############################################################################
def concatenate(l):
    out = ""
    for x in l:
        out = out + str(x)
    return int(out)

def largestConcat(l):
    """
    >>> largestConcat([1,2,55,3])
    55321
    """
    num = 0
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            if(l[i] < l[j]):    
                temp = l[i];    
                l[i] = l[j];    
                l[j] = temp;  

    num = concatenate(l)
    return num 
    pass


############################################################################
#
# Problem 3
# Write a function to return the number of unique elements in an array.
# for example the list [3,6,2,3,2,7,4] has 3 unique elements, 6, 7, and 4.
#
# Running Time: 0(n)
############################################################################
def numberUnique(l):
    """
    >>> numberUnique([3,6,2,3,2,7,4])
    3
    """
    l1 = []
    count = 0

    # Pick all elements one by one
    for item in l:
        if item not in l1:
            count += 1
            l1.append(item)
        elif item in l1:
            count -= 1
            l1.append(item)
     
    return count
    pass


############################################################################
#
# Problem 4
# Implement insertion sort from class.
#
# Running Time: O(n^2)
############################################################################
import numpy as np
def insertionSort(l):
    """
    >>> insertionSort([3,6,2,5,1])
    [1, 2, 3, 5, 6]
    """
    for i in range(1, len(l)):
        key = l[i]
        j = i-1

        while j >=0 and key < l[j] :
                l[j+1] = l[j]
                j -= 1
        l[j+1] = key


    return l
    pass

############################################################################
#
# Problem 5
# Use the heap from last homework to sort an array.
#
# Running Time: O(log n)
############################################################################
def heapSort(n):
    """
    >>> heapSort([3,6,2,5,1])
    [1, 2, 3, 5, 6]
    """
    r = len(n)

    # Build a maxheap.
    for i in range(r//2 - 1, -1, -1):
        re_heap(n, r, i)
 
    # One by one extract elements
    for i in range(r-1, 0, -1):
        n[i], n[0] = n[0], n[i]  # swap
        re_heap(n, i, 0)

    return n
    pass

def re_heap(arr, n, i):
    largest = i  
    l = 2 * i + 1   
    r = 2 * i + 2
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 

        re_heap(arr, n, largest)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
