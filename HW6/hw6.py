# CS 350: Homework 6
# Due: Week of 6/16
# Name: Andrey Toderyan

import math
from itertools import product

def machine(data, code):
    i = 0
    value = 0
    for instruction in code:
        if i >= len(data):
            raise Exception("Ran out of numbers")
        if instruction == "ADD":
            value += data[i]
            i += 1
        elif instruction == "MUL":
            value += data[i] * data[i+1]
            i += 2
        else:
            raise Exception("Illegal Instruction: " + instruction)
    if i < len(data):
        raise Exception("has leftover numbers")
    return value

###########################################################################
# Problem 1:

# I've constructed a new data processing language that I call addmul.
# It is a very simple language, programs in addmul consist of two instructions.
# ADD take a value from the data stream and adds it to the current total
# MUL takes the next two number from the current data stream, multiplies them together,
# and adds them to the total.
# That's it.

# Your job is to take the data stream (just a list of numbers), and determine
# the program that will produce the largest value.

# example:
# largetstProgram([2,3,5])
# should return
# ["ADD","MUL"]
# because this will return 17
# where ["MUL","ADD"] will return 11
# and ["ADD","ADD","ADD"] will return 10

# You can run your program by calling 
# machine([2,3,4], ["ADD","MULL]) 
# to run your program

# you can use
# machine(numbers, largestProgram(numbers))
# to test your algorithm on any list of numbers.

# running time: 0(n^2)
###########################################################################
import math
from itertools import product

def machine(data,code):
    i = 0
    value = 0
    for instruction in code:
            if i >= len(data): raise Exception("Ran out of numbers")
            if instruction == "ADD":
                    value += data[i]
                    i += 1
            elif instruction == "MUL":
                    value += data[i] * data[i+1]
                    i += 2
            else: raise Exception("Illegal Instruction: "+instruction)

    if i<len(data):
            raise Exception("has leftover numbers")

    return value

def largestProgram(data):
    """
    >>> largestProgram([2,3,5])
    ['ADD', 'MUL']
    """
    
    # Variables to store max value and code
    max_val = float('-inf')
    max_code = None

    # Instructions and values
    instrunctions = {'ADD':1, 'MUL':2}

    # Loop over all combinations
    for k in range(1,len(data)+1):
            codes = list(product(instrunctions.keys(),repeat=k))

            # For each code generated
            for code in codes:

                    # Find if valid code is produced
                    sum_code = 0
                    for instr in code:
                            sum_code += instrunctions[instr]

                    # If code is valid, calculate value
                    if(sum_code==len(data)):
                            code = list(code)
                            value = machine(data,code)

                            # If value if bigger than current max
                            # Update max value and code
                            if(value>max_val):
                                    max_val = value
                                    max_code = code

    # Return Max Code
    return max_code

##########################################################################
# Problem 2

# Implemnt the Floyd-Warshal algorithm from class

# For example, the adjacency matrix:
#    [ [  0, inf,  -2, inf], 
#      [  4,   0,   3, inf], 
#      [inf, inf,   0,   2], 
#      [inf,  -1, inf,   0] ]
# should give the distance matrix:
#    [ [  0,  -1,  -2,   0], 
#      [  4,   0,   2,   4], 
#      [  5,   1,   0,   2], 
#      [  3,  -1,   1,   0] ]


# Running Time: 0 (n^3)
##########################################################################
# Working procedure of the Floyd Warshall Algorithm 
#importing the math library to use the math.inf 
import math
# The number of vertices
nV = 4
#defining the math.inf as inf
inf = math.inf
# Algorithm implementation

def floyd(G):
    """
    >>> floyd([ [0, math.inf, -2, math.inf], [4, 0, 3, math.inf], [math.inf, math.inf, 0, 2], [math.inf, -1, math.inf, 0]])
    [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
    """
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance
    
    pass



###########################################################################
# Problem 3

# Congratulations! You know own a factory that cuts rods.
# Customers will pay a certain value for a length of rods
# for example
# rod length:  3  4  5  6   7
# price:       2  3  6  8  11

# You just received a rod of length d, 
# Write a function to determine the most efficient way to cut the rod
# to maximize the profit.
# You should return the maximum profit you can make.

# Running Time: 0(n^2)
###########################################################################

def rods(weights, prices, d):
    """
    >>> rods([3,4,5,6,7], [2,3,6,8,11], 20)
    30
    """
    dp = [0] * (d+1)
	
	# looping over d to calculate the efficient way to cut the rod for each length till d
    for i in range(1, d+1):
	    # looping over each length to check if the cutting the rod by length is profitable
	    for j in range(len(weights)):
		    length = weights[j]
			# i-length is positive then we can cut the rod by length
		    if i - length >= 0:
			    # checking if cutting the rod by length is profitable by taking max value of two
			    dp[i] = max(dp[i], dp[i - length] + prices[j])

	# finally returning dp[d] to check the max profit for a rod of length d
    return dp[d]
    
    pass

############################################################################
# Problem 4: Parenthesizing matrices.

# This is the same problem as homework 4, problem 3,
# but this time I want you to do it in polynomial time using dynamic programmign.

# If I multiply and m*l matrix A by an l*n matrix B
# That will take O(n*l*m) time to compute.

# If I include a n*o matrix C in this product
# Then I have the m*o matrix A*B*C.
# This is perfectly well defined, but I have a choice.
# Do I multiply (A*B)*C (giving a running time of n*l*m + n*m*o)
# or do i multiply A*(B*C) (giving a running time of l*m*o + n*l*o)

# Since matrix multiplication is associative, We will get the same answer.

# So, given a list of dimensions of matrices
# (for example [(n,l), (l,m), (m,o)])
# compute the fastest running time that we can do matrix multiplication in. 

# example [(3,5), (5,4), (4,7)]
# is 3*5*4 + 3*4*7 = 144

# Running time: 0(n^2)
############################################################################
def matrixParens(matrix_input):
    # """
    # >>> matrixParens([[3,5], [5,4], [4,7]])
    # 144
    # """
    # Getting the length and width (shape of the matrix)

    input_rows = len(matrix_input)
    input_columns = len(matrix_input[0])

    # Creating a new matrix with all 0's of the same shape as matrix_input

    matrix_result = [[0 for i in range(input_columns)] for i in range(input_rows)]

    # Fill in the diagnol values

    for i in range(input_rows):
        for j in range(input_columns):
            matrix_result[i][i] += matrix_input[i][j] * matrix_input[i][j]
                
    b = 0
    c = 0

    # Find rest values and copy them

    for i in range(1, input_rows):
        while c < i and b < input_columns:
            matrix_result[i][c] += matrix_input[i][b] * matrix_input[c][b]
            b += 1
            if ( b >= input_columns):
                c += 1
                b = 0
            matrix_result[c-1][i] = matrix_result[i][c-1]
    b = 0
    c = 0

    # Print the resultant matrix

    for i in range(input_rows):
        for j in range(input_columns):
            print(f'{matrix_result[i][j]}\t', end="")

    print("")

    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
