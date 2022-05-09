# https://stackoverflow.com/questions/47004506/check-if-a-numpy-array-is-sorted
# https://www.dropbox.com/sh/ftzvcnntl2j5eiu/AAASovmq047jOClaHjL4h4GIa?dl=0&preview=2__Blind+Search_part1.pptx
import numpy as np
import queue

def goal_test(board):
    return np.all(board[:-1] <= board[1:])
# computationally intractable without heuristics
def bfs(initial):
    # Each state is a 2-tuple (1) board state (2) list of swaps
    frontier = queue.Queue()
    frontier.put((tuple(initial),()))
    explored = set()
    while(True):
        if frontier.empty(): return 'failure'
        curr,swaps = frontier.get()
        ops = list(swaps)
        if goal_test(np.array(curr)): return curr,swaps
        c = np.array(curr)
        for swap1 in range(len(c)):
            for swap2 in range(swap1,len(c)):
                c[swap1],c[swap2] = c[swap2],c[swap1]
                if tuple(c) not in explored:
                    explored.add(tuple(c))
                    ops.append((swap1,swap2))
                    frontier.put((tuple(c),tuple(ops)))

a = np.arange(25)
np.random.shuffle(a)
print(bfs(a))




