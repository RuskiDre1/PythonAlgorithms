# CS 350: Homework 1
# Due: Week of 4/4
# Name: Andrey Toderyan
#We have this problem why are the outside of the song yes there anything about
# This homework is largely review, and to make sure you have a working version of python.
import math

############################################################################
#
# Problem 1
# Find the largest two elements in a list.
# Return your answer in a tuple as (largest, secondLargest)
#
# Running Time: 0(n^2)
############################################################################
def largest2(l):
    """
    >>> largest2([1, 2, 3, 4, 5, 6, 7])
    (7, 6)
    >>> largest2([7, 6, 5, 4, 3, 2, 1])
    (7, 6)
    
    """
    first = l[0]
    second = l[0]
    

    #loop once and when largest changes then second adopts
    #previous largest
    for x in l:
        if x > first:
            second = first
            first = x
    second = 0
    for x in l:
        if x < first and x > second:
            second = x

    tup1 = (first, second)

    return (first, second)

    pass

#g = [1, 2, 3, 4, 5, 6, 7]
#largest2(g)

# ############################################################################
# #
# # Problem 2
# # Reverse a list in place,
# # and returned the reversed list.
# #
#new_lst = l[::-1]
 #   return new_lst
# # Running Time: 0(n^2)
# ############################################################################

def reverse(l):
    """
    >>> l = [1, 2, 3, 4, 5]
    >>> reverse(l)
    [5, 4, 3, 2, 1]
    >>> l
    [5, 4, 3, 2, 1]
    """
    
    g = []
    for i in range(len(l)):
        g.insert(0,l[i])

    for i in range(len(g)):
        l[i] = g[i]
    

    return l
    pass
# v = [1, 2, 3, 4, 5]
# reverse(v)

# for e in range(5):
#     print(v[e])
    
# ############################################################################
# #
# # Problem 3
# # Compute the transpose of a matrix in place.
# #
# # What is the input size measuring? r x m ,3 x 3
# # Running Time: O(n^2)
# ############################################################################

def transpose(m):
    """
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> transpose(m)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    >>> m
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """

   
    #result = [[0,0,0],[0,0,0],[0,0,0]]

    result = [[0 for j in range(len(m))] for i in range(len(m[0] ))]


     # iterate through rows
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]

    for i in range(len(result)):
        for j in range(len(result[0])):
            m[i][j] = result[i][j]
            
    return m

    pass


############################################################################
#
# Problem 4
# Given a list of points, return the distance between the two closest points.
# The distance between two points (x1,y1) and (x2,y2) is:
# d = sqrt((x2-x1)^2 + (y2-y1)^2)
#
# Running Time:  O(1)
############################################################################

def pointDist(points):
    """
    >>> pointDist([(1,1), (4,5), (13,6)])
    5
    """
    #tup[j][0]
    #calculate the distance between each set of points

    #1 and 2
    x1 = points[0][0]
    y1 = points[0][1]
    x2 = points[1][0]
    y2 = points[1][1]
 
    one = math.sqrt(  ((x2-x1)**2) + ((y2-y1)**2)   ) 
    #1 and 3
    x2 = points[2][0]
    y2 = points[2][1]
    two = (  ((x2-x1)**2) + ((y2-y1)**2)   ) **0.5
    # 2 and 3
    x1 = points[1][0]
    y1 = points[1][1]
    three = (  ((x2-x1)**2) + ((y2-y1)**2)   ) **0.5
    
    #print(one, two, three)
    if one < two:
        if one < three:
            return int(one)
        if two < three:
            return  int(two)
        return int(three)

    pass

############################################################################
#
# Problem 5
# multiply two matrices A and B.
# For the running time A is an m*n matrix, and B is an n*l matrix.
#
# what is the size of the output? ?*?
# Running Time: O(n^3)
############################################################################

def matMul(A,B):
    """
    >>> matMul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]
    """
    a_row = len(A)
    a_col = len(A[0])

    b_row = len(B)
    b_col = len(B[0])
    #   [[1, 2, 3]
    #   [4, 5, 6]]
      
      
    #   [[7, 8]
    #   [9, 10]
    #   [11, 12]]

    #mat = [[0 for _ in range(cols)] for _ in range(rows)]
    mat = []
    for i in range(0,len(A)):
        temp=[]
        for j in range(0,len(B[0])):
            s = 0
            for k in range(0,len(A[0])):
                s += A[i][k]*B[k][j]
            temp.append(s)
        mat.append(temp)

    return mat

    # run thru each row and multiply to get number

    
    
    pass
#print(matMul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))


# ############################################################################
# #
# # Problem 6
# # Compute the number of 1s that would be in the binary representation of x
# # for example: 30 = 11110 in base 2, and it has 4 1s.
# #
# # For full credit, you should assume that 
# # arithmetic operations are *not* constant time.
# # bitwise operations are constant time though.
# #
# # What is the input size? 1
# # Running Time: O(logn)
# ############################################################################

def popcount(x):
    """
    >>> popcount(7)
    3
    >>> popcount(30)
    4
    >>> popcount(256)
    1
    """
    counter = 0
    
    i = 1 << 31 #set all to 1
    while(i > 0) :
        if((x & i) != 0) :
            counter += 1
        i = i // 2

    return counter

    pass


# ############################################################################
# #
# # Problem 7
# # compute the integer square root of x.
# # This is the largest number s such that s^2 <= x.
# #
# # You can assume that arithmetic operations are constant time for this algorithm.
# #
# # What is the input size? 1
# # Running Time: O(logn)
# ############################################################################

def isqrt(x):
    """
    >>> isqrt(6)
    2
    >>> isqrt(121)
    11
    >>> isqrt(64)
    8
    """

    i = 1
    result = 1
    while (result <= x):
        i += 1
        result = i * i
     
    return i - 1

    pass

# ############################################################################
# #
# # Problem 8: Word Search
# #
# # determine if string s is any where in the word grid g.
# #
# # for example s = "bats"
# # g = ["abrql",
# #      "exayi",
# #      "postn",
# #      "cbkrs"]
# #
# # Then s is in the word grid
# #     [" b   ",
# #      "  a  ",
# #      "   t ",
# #      "    s"]
# #
# # what is your input size? 4 x 5
# # Running Time: O(n^3)
# ############################################################################

def wordSearch(word,grid):
    """
    >>> s = "bats"
    >>> g = ["abrql", "exayi", "postn", "cbkrs"]
    >>> wordSearch(s,g)
    True
    """
    x = 0
    y = 0
    
    grid_y =len(grid)
    grid_x = len(grid[0])


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == word[0]):
                x = i
                y = j
    
    #check the boundries around start point;
    i = 1
 
    check = 0
    while(i < len(word) and check == 0):
        if(grid[x-1][y+1] == word[i]):
            x-=1;y+=1;i+=1
        elif( x+1 < 0 and grid[x+1][y-1]== word[i]):
            x+= 1; y-= 1 ;i+=1;            
        elif(grid[x][y-1] and grid[x][y-1]== word[i]):
            y-=1;i+=1;           
        elif(grid[x-1][y] and grid[x-1][y] == word[i]):
            x-=1;i+=1
        elif(grid[x][y+1] and grid[x][y+1] == word[i]):
            y += 1;i+=1
        elif( x+1 < 0 and grid[x+1][y+1]== word[i]):
            x+= 1; y+= 1;i+=1
        elif(x+1 < 0 and grid[x+1][y]== word[i]):
            x+= 1; i+=1
        elif(grid[x-1][y-1] == word[i]):
            x-=1;y+=1;i+=1
        else:
            check = 1

      
    
    if(check == 0):
        return False
    return True
       
        


    pass

# ############################################################################
# #
# # Problem 9: Convex Hull
# #
# # In class we learned about the convex hull problem.
# # We also learned that for any line segment on the convex hull,
# # every other point will we on the same side of that line.
# #
# # Use this fact to write an algorithm to find all of the points in the convex hull.
# #
# # for example: [(1,1), (4,2), (4,5), (7,1)] are the points shown below
# #
# #    *
# #
# #    *
# # *     *
# #
# # The convex hull is [(1,1), (4,5), (7,1)]
# #    *
# #   / \
# #  /   \
# # *-----*
# #
# # Running Time: 
# ############################################################################

# def convexHull(points):
#     """
#     >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
#     [(1, 1), (4, 5), (7, 1)]


#     """

    


#     pass


# ############################################################################
# #
# # Problem 10: Running time
# #
# # Find the Theta time complexity for the following functions.
# # If the problem is a summation, give a closed form first.
# #
# # 1. f(n) = n^2 + 2n + 1
#   O(n^2)

# # 2. f(n) = sum(i=0, n, sum(j=0, i, 1) )
#   1 + 2 + 3 + ... n = n * (n + 1) / 2 = O(n^2)

# # 3. f(n) = (n+1)!
#    (n+ 1)! = (n+1) * n! = O(n!)

# # 4. f(n) = sum(i=0, n, log(i))
#   log(1) + log(2) + log(3) + ... log(n) = O(nlogn)

# # 5. f(n) = log(n!)
#   log(n^n) = O(nlogn)
# ############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
