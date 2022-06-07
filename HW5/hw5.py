# CS 350: Homework 5
# Due: Week of 5/9
# Name: Andrey Toderyan

# You should not assume anything about the data for these problems
# other than it's valid.
# Adjacency lists might not be in any particular order
# and graphs may not be connected.

############################################################################
#
# Problem 1
#
# write a function that returns the set of connected components 
# of an undirected graph g.
# g is represented as an adjacency list
# you should return a list of components, where each component is a list of vertices.
# Example g = [[1,2], [0,2], [0,1], [4], [3]]
# Should return a list of two components [[0,1,2],[3,4]]

# Running time? 0(n)
def components(g):
    """
    >>> components([[1,2], [0,2], [0,1], [4], [3]])
    [4, 3]
    """
    comps = [[]]
    travel = [0] * len(g) 
 
    while 0 in travel:
        vertex  = travel.index(0)
        comp = graph(g, vertex, travel) 
        comps.append(comp)

    del comps[0]
    return comp
def graph(g, vectex, travel):
    i = 0
    comp = []
    travel[vectex] = 1
    while i < len(g[vectex]):
        node = g[vectex][i]
        if travel[node] == 0:
            comp = graph(g, g[vectex][i], travel)
        i += 1
    comp.append(vectex)

    return comp
############################################################################
#
# Problem 2
#
# write a function the returns True if, and only if, graph g is bipartite
# g is represented as an adjacency list

# Running time?
#
############################################################################

def bipartite(array):
    """
    >>> bipartite([[3,4,7], [3,5,6], [4,5,7], [0,1], [0,2], [1,2], [1], [0,2]])
    True
    """
    adjacent = []
    
    for i in range(len(array)):
        adjacent.append(array[i])
    vertices = len(adjacent)
    print(check(vertices, adjacent))


def check(vertices, adjacent):
    flag = [None]*(vertices)
    red = 0
    black = 1

    array_g = []

    for i in range(vertices):
        if (flag[i] == None):

            array_g.append([i, red])
            flag[i] = red

            while len(array_g) != 0:
                currentBFS = array_g[red]
                del array_g[0]
                vertices = currentBFS[red]
                currentflag = currentBFS[black]

                for j in adjacent[vertices]:
                    if (flag[j] == currentflag):
                        return False
                    if (flag[j] == None):
                        if currentflag == black:
                            flag[j] = red
                        else:
                            flag[j] = black
                        array_g.append([j, flag[j]])
    return True

    pass
############################################################################
#
# Problem 3

# write a function the returns True if, and only if, graph g is a forrest
# g is represented by a adjacency list.

# Running time? 0^2

############################################################################

def isForrest(array):
    """
    >>> isForrest([[1,2], [3,4], [5,6], [], [], [], []])
    True
    >>> isForrest([[1,2], [3,4], [5,4], [], [], []])
    False
    """
    uniquelist = []
    check = []

    for i in range(len(array)):
        for j in range(len(array[i])):
            check.append(array[i][j])
    check.sort()

    for elem in check:
        if elem in uniquelist:
            pass
        else:
            uniquelist.append(elem)
    size = len(uniquelist)-1

    for i in range(len(check)):
        count = 0
        for j in range(len(check)-1):
            if check[i] == check[j+1]:
                count += 1

    if count >= size or len(uniquelist) != len(check):
        print("False")
    else:
        print("True")

    pass

############################################################################
#
# Problem 4

# write a function to topologically sort the vertices of a directed graph d
# Assume d is an adjacency list.

# Running time? O ^ 2

############################################################################
def topsort(arr):
    """
    >>> topsort([[1, 2], [3], [3], []])
    [0, 1, 2, 3]
    """
    graph = {}
    count = {}
    # creates the adjacency list of graph
    for i in range(len(arr)):
        graph[i] = arr[i]
        count[i] = 0
    # counts the degree of the each node in the graph
    for i in range(len(arr)):
        for ver in arr[i]:
            count[ver] += 1
    queue = []
    visited = set()
    # appends the nodes whose degree is 0
    for i in range(len(arr)):
        if count[i] == 0:
            queue.append(i)
            visited.add(i)
    res = []
    # finds the topological order the graph
    while queue:
        curr = queue.pop(0)
        res.append(curr)
        for ver in graph[curr]:
            count[ver] -= 1
            if ver not in visited and count[ver] == 0:
                queue.append(ver)
                visited.add(ver)
    # returns the topological order
    return res
    
    pass

############################################################################
#
# Problem 5

# write a function to determine the strongly connected components of digraph d.
# Just like the components example, you should return a list of strongly connected components.

# Running time? O ^ 2
def scc(d):
    """
    >>> scc([[1], [2], [0,3], [1,2], [3,5,6], [4], [7], [8], [6]])
    [[3, 2, 1, 0], [8, 7, 6, 4]]
    """
    travel = [0] * len(d)
    vertex = 0
    comp = []
    answer = findScc(d, vertex, travel)
    comp.append(answer)

    while 0 in travel:
        vertex  = travel.index(0)
        answer = findScc(d, vertex, travel)
        comp.append(answer)
    return comp
    pass
def findScc(d, vertex, travel):
    i = 0
    travel[vertex] = 1
    comp = []
    while i < len(d[vertex]):
        node = d[vertex][i]

        if travel[node] == 0:
            comp = findScc(d, node, travel)
        i += 1
    comp.append(vertex)
    return comp


############################################################################

# Problem 6

# # a. What doe we need to change about BFS/DFS if we use an adjacency matrix?
# In adjacency matrix representation of a graph, the matrix mat[][] of size n*n 
# (where n is the number of vertices) will represent the edges of the graph where mat[i][j] = 1 
# represents that there is an edge between the vertices i and j while mat[i][j] = 0 
# represents that there is no edge between the vertices i and j.
# # b. What is the running time for BFS/DFS if we use and adjacency matrix?
# The Time complexity of BFS is O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used, where V stands for vertices and E stands for edges.

# The Time complexity of DFS is also O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used, where V stands for vertices and E stands for edges.
# Note that each row in an adjacency matrix corresponds to a node in the graph, 
# and that row stores information about edges emerging from the node. 
# Hence, the time complexity of DFS in this case is O(V * V) = O(V2).
# # c. Give an example of a weighted graph where BFS doesn't return the shortes path.
# #BFS is the algorithm to use if we want to find the shortest path in an undirected, unweighted graph. The claim for BFS is that the first time a node is discovered during the traversal, that distance from the source would give us the shortest path.

# The same cannot be said for a weighted graph. Consider the graph above. If say we were to find the shortest path from the node A to B in the undirected version of the graph, 
# then the shortest path would be the direct link between A and B. So, the shortest path would be of length 1 and BFS would correctly find this for us.

# So, the first discovery of a node during traversal does not guarantee the shortest path for that node. For example, in the diagram above, the node B would be discovered initially 
# because it is the neighbor of A and the cost associated with this path (an edge in this case) would be 25 . But, this is not the shortest path. The shortest path is A --> M --> E --> B 
# of length 10.

# Breadth first search has no way of knowing if a particular discovery of a node would give us the shortest path to that node. And so, the only possible way for BFS (or DFS) to find the 
# shortest path in a weighted graph is to search the entire graph and keep recording the minimum distance from source to the destination vertex.
############################################################################


if __name__ == "__main__":
    import doctest
    doctest.testmod()