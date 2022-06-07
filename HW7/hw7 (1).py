#Andrey Toderyan

################################################################
# Problem 1

# We're going to take the job scheduling problem from class,
# but this time, I want to make sure every job is scheduled.
# If I have a set of n jobs where each job is represented
# by a tuple (s,f),
# Give a greedy algorithm to schdule the jobs on the fewest
# number of processors total

# Running Time: 0(n)
# ###############################################################

def schedule(jobs):
    
    """  
    >>> schedule([(5,40), (30,35), (6,20), (19, 31), (23, 29), (28, 32)])
    [[(6, 20), (23, 29), (30, 35)], [(19, 31)], [(28, 32)], [(5, 40)]]
    """
    
    if len(jobs)==0:
        return []
    jobs2=sorted(jobs,key=lambda x:x[1])
    arr = []
    i=0
    times=0
    temp=[]
    while times<len(jobs2):            
        if len(temp)==0:
            temp.append(jobs2[i])
            i+=1
        else:
            if temp[-1][1] <= jobs2[i][0]:
                temp.append(jobs2[i])
                i+=1
            else:                   
                j=jobs2.pop(i)
                jobs2.append(j)
        times+=1 
    
    arr.append(temp)

    furthur =schedule(jobs2[len(temp):])             
    if(len(furthur)>0):
        arr = arr + furthur
    return arr 

################################################################
# Problem 2

# Given a list of string (strings)
# Find s short string (bigstring) that 
# for every s in string, s is a substring of bigstring.

# Use the approximation algorithm we gave in class.

# Running Time: 0(n^2)
###############################################################
from functools import lru_cache
from itertools import permutations


def superstring(strings):
    """
    >>> superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
    'BCDAABDDCADBCADC'
    """

    test = Solution()
    return test.shortestSuperstring(strings)

    pass

class Solution:
    def shortestSuperstring(self, A):
        @lru_cache(None)
        def connect(w1, w2):
            return [(w2[i:], len(w2) - i) for i in range(len(w1) + 1) if w1[-i:] == w2[:i] or not i][-1]
        
        N = len(A)
        dp = [[(float("inf"), -1)] * N for _ in range(1<<N)]
        for i in range(N): dp[1<<i][i] = (len(A[i]), -1)
            
        for mask in range(1<<N):
            n_z_bits = [j for j in range(N) if mask & 1<<j]
            for j, k in permutations(n_z_bits, 2):
                dp[mask][j] = min(dp[mask][j], (dp[mask ^ 1<<j][k][0] + connect(A[k], A[j])[1], k))
                
        mask = (1<<N) - 1
        prev = min(dp[mask])
        last = dp[mask].index(prev)
        prev = prev[1]
        ans = ""
        
        while prev != -1:
            ans = connect(A[prev], A[last])[0] + ans
            mask -= (1<<last)
            prev, last = dp[mask][prev][1], prev
            
        return A[last] + ans

################################################################
# Problem 3

# Find the shortest path from a to b
# in a weighted graph g that is represented by an adjacency matrix.
# You can assume all edge weights are positive.

# Running time: O(elogv)
###############################################################
def dijkstra(g, a, b):
    """
    >>> g = [ [(1,3), (2,6)], \
              [(0,3), (4,4)], \
              [(0,6), (3,2), (5,7)], \
              [(2,2), (4,4), (8,1)], \
              [(1,4), (3,4), (6,9)], \
              [(2,7), (6,2), (7,8)], \
              [(4,9), (5,2), (9,4)], \
              [(5,8), (8,3)], \
              [(3,1), (7,3), (9,2)], \
              [(6,4), (8,2)] ]
    >>> dijkstra(g,0,9)
    [0, 2, 3, 8, 9]
    """
    nodes = [math.inf] * len(g) #weight to get to that node
    visited = [False] * len(g) #nodes that were visited
    parent = [None] * len(g) #connection node
    queue = [] 
    queue.append(a)
    nodes[a] = 0

    while len(queue) != 0:
        vertex = queue[0] 
        visited[vertex] = True
        for node, weight in g[vertex]: 
            if visited[node] == False:
                if nodes[node] == math.inf: 
                    nodes[node] = nodes[vertex] + weight
                    parent[node] = vertex
                if node not in queue:
                    queue.append(node)
            if nodes[vertex] + weight < nodes[node]: 
                parent[node] = vertex
                nodes[node] = nodes[vertex] + weight
        queue.pop(0)
    answer = []

    while a != b:
        if a == b: break
        answer = [b] + answer
        b = parent[b]
    answer = [b] + answer
    return answer
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
