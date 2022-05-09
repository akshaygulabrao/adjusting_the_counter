# https://stackoverflow.com/questions/47004506/check-if-a-numpy-array-is-sorted
# https://www.dropbox.com/sh/ftzvcnntl2j5eiu/AAASovmq047jOClaHjL4h4GIa?dl=0&preview=2__Blind+Search_part1.pptx
# https://docs.python.org/3/library/heapq.html
import numpy as np
import heapq

def goal_test(a):
    return (a == np.sort(a)).all()

# computationally intractable without heuristics
def ucs(initial):
    # Each state is a 2-tuple (1) board state (2) list of swaps
    initial_state = (0,0,initial,[])
    h = []
    heapq.heappush(h,initial_state)
    explored = set()
    explored.add(tuple(initial))
    while(True):
        # print(explored)
        if not len(h):
            # print(explored)
            return 'failure'
        depth,heuristic,curr,swaps = heapq.heappop(h)
        print(curr)
        # print(depth, heuristic, curr, swaps)
        # print('gas')
        if goal_test(curr):
            return 'success'
        for i in range(0,len(curr)):
            for j in range(i,len(curr)):
                d = np.copy(curr)
                d[i],d[j] = d[j],d[i]
                if tuple(d) not in explored:
                    explored.add(tuple(d))
                    nL = swaps.copy()
                    nL.append((i,j))
                    heapq.heappush(h,(depth+1,0,list(d),nL))
a = np.arange(5)
np.random.shuffle(a)
print(ucs(a))



