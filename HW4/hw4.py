# CS 350: Homework 4
# Due: Week of 4/4
# Name: Andrey Toderyan

############################################################################
# Problem 1: Quicksort
# 
# implement quicksort described in class.
#
# Recurrence worst case: T(n) = T(n-1) + O(n)
# Recurrence average case: O(nLogn)
# Running time worst case: O(N^2)
# Running time average case:  T(n) = 2T(n/2) + \theta(n)
# 
# When does the worst case happen?
# one of the two sublists is empty
############################################################################

def quicksort(l):
    """
    >>> quicksort([3,2,6,1,4])
    [1, 2, 3, 4, 6]
    >>> quicksort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    """
    return quick_sort(l, 0, len(l) - 1)

    pass

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    
     
    # Recursive call on the left of pivot
    # Recursive call on the right of pivot
   

    return array

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot: 
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    
    (array[i + 1], array[high]) = (array[high], array[i + 1])
        
    return i + 1


############################################################################
# Problem 2: maximum sublist sum
# 
# A sublist is a contiguous piece of a list
# [1,2,1] is a sublist of [4,1,2,1,3]
# but [1,2,3] isn't.
#
# the sum of a list is just adding all of the elements.
#
# compute the maximum sum of any sublist.
# For example:  [-2,1,-3,4,-1,2,1,-5,4]
# the maximum sublist is [4,-1,2,1] with a sum of 6
# 
# Running time: 0(n)
############################################################################
def maxSublist(nums):
    """
    >>> maxSublist([-2,1,-3,4,-1,2,1,-5,4])
    [4, -1, 2, 1]
    """

    currMax = nums[0]
    globalMax = nums[0]

    for i in range(1, len(nums)):
 
        currMax = max(nums[i],
                      nums[i] + currMax)
 
        if (currMax > globalMax):
            globalMax = currMax
            endIndex = i
     
    startIndex = endIndex
 
    while (startIndex >= 0):
        globalMax -= nums[startIndex]
 
        if (globalMax == 0):
            break

        startIndex -= 1


    l = []
    for i in range(startIndex, endIndex + 1):
        l.append(nums[i])
        #print(nums[i], end = " ")
    return l
    pass

############################################################################
# Problem 3: Parenthesizing matrices.
# 
# If I multiply and m*l matrix A by an l*n matrix B
# That will take O(n*l*m) time to compute.
#
# If I include a n*o matrix C in this product
# Then I have the m*o matrix A*B*C.
# This is perfectly well defined, but I have a choice.
# Do I multiply (A*B)*C (giving a running time of n*l*m + n*m*o)
# or do i multiply A*(B*C) (giving a running time of l*m*o + n*l*o)
#
# Since matrix multiplication is associative, We will get the same answer.
#
# So, given a list of dimensions of matrices
# (for example [(n,l), (l,m), (m,o)])
# compute the fastest running time that we can do matrix multiplication in. 
#
# example [(3,5), (5,4), (4,7)]
# is 3*5*4 + 3*4*7 = 144
# 
# Running time: 0(1)
############################################################################
def matrixParens(sizes):
    """
    >>> matrixParens([(3,5), (5,4), (4,7)])
    144
    """
    # extracting n, l, m and o values from sizes
    n, l = sizes[0]
    l, m = sizes[1]
    m, o = sizes[2]

    # caculating fastest running time
    return n*l*m + n*m*o

    pass

############################################################################
# Problem 4: Convex Hull again!
# 
# Use the Divide and Conquer algorithm described in class to compute
# the convex hull of a set of points.
#
# Recurrence worst case:
# Recurrence average case:
# Running time worst case:
# Running time average case:
# 
# When does the worst case happen?
############################################################################

def convexHull(points):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    """

    l = ConvexHull(points)
    return l.hull
    
    
#     points = sorted(points, key = lambda p: points.x)

#     convex_hull(points)
#     return points

# def convex_hull(points):
#     if len(points) == 1:
#         return points

#     left_half = convex_hull(points[0: len(points)/2])
#     right_half = convex_hull(points[len(points)/2:])
#     return merge(left_half, right_half)



class ConvexHull:
	def __init__(self, points):
		if not points:
			self.points = [(0,0)]
		else:
			self.points = points
		self.hull = self.compute_convex_hull()
    
	def get_cross_product(self,p1, p2, p3):
		return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))

	def get_slope(self,p1, p2):
		if p1[0] == p2[0]:
			return float('inf')
		else:
			return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])

	def compute_convex_hull(self):
		hull = []
		self.points.sort(key=lambda x:[x[0],x[1]])
		start = self.points.pop(0)
		hull.append(start)
		self.points.sort(key=lambda p: (self.get_slope(p,start), -p[1],p[0]))
		for pt in self.points:
			hull.append(pt)
			while len(hull) > 2 and self.get_cross_product(hull[-3],hull[-2],hull[-1]) < 0:
				hull.pop(-2)
		return hull
############################################################################
# Problem 5: Recurrence relations

# Give a closed form, and bit Theta for the following recurrence relations.
# If it's a divide and conquer relation, then you only need to give the Theta.

# a. Give the recurrence relation for Karatsuba's algorithm, and solve it.
#
#   T(n) = 3T(n/2) + O(n)
#   T(n) = aT(n/b) + d(n)
#   a = 3 b = 2
#   d(n) = O(n) and 1 < Log2 (3)
#   T(n) = O(n ^ Log2 (3))
# b. Give the recurrence relation for Strassen's algorithm, and solve it.
#
#   T(n) = O(n ^ log2 (7) )
# c.
#
# T(1) = 1
# T(n) = T(n-1) + n
#
#   T(n-2) + n-1 + n
#   O(n^2)
#
# d. 
# T(1) = 1
# T(n) = 2T(n-2) + 1
#   O(2 ^ n)
# 
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
