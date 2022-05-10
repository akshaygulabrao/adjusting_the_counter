# https://stackoverflow.com/questions/47004506/check-if-a-numpy-array-is-sorted
# https://www.dropbox.com/sh/ftzvcnntl2j5eiu/AAASovmq047jOClaHjL4h4GIa?dl=0&preview=2__Blind+Search_part1.pptx
# https://docs.python.org/3/library/heapq.html

import numpy as np
import heapq
import matplotlib.pyplot as plt
def goal_test(a):
    a = np.array(a)
    return np.array_equal(np.array(a),np.arange(a.shape[0]))

def correct_number_heuristic(a):
    return np.count_nonzero(a!=np.arange(a.shape[0]))

def akshay_heuristic(state,swaps):
    return correct_number_heuristic(a) * 2


# computationally intractable without heuristics
def ucs(initial):
    # Each state is a 2-tuple (1) board state (2) list of swaps
    initial_state = (0,0,initial,[])
    h = []
    heapq.heappush(h,initial_state)
    explored = set()
    explored.add(tuple(initial))
    while(True):
        if not len(h):
            return 'failure'
        depth,heuristic,curr,swaps = heapq.heappop(h)
        print(depth,curr,swaps)
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
def akshay(initial):
    initial_state = (0,0,initial,[])
    h = []
    heapq.heappush(h,initial_state)
    explored = set()
    explored.add(tuple(initial))
    while(True):
        if not len(h):
            return 'failure'
        depth,heuristic,curr,swaps = heapq.heappop(h)
        print(depth,curr,swaps)
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
                    heapq.heappush(h,(akshay_heuristic(d,nL)+depth+1,0,list(d),nL))

def correct_tile_heuristic(initial):
    # Each state is a 2-tuple (1) board state (2) list of swaps
    initial_state = (correct_number_heuristic(a),0,initial,[])
    h = []
    heapq.heappush(h,initial_state)
    explored = set()
    explored.add(tuple(initial))
    while(True):
        if not len(h):
            return 'failure'
        depth,heuristic,curr,swaps = heapq.heappop(h)
        print(depth,curr,swaps)
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
                    heapq.heappush(h,(correct_number_heuristic(d),0,list(d),nL))



print("Akshay Gulabrao 862007974: Adjusting the Counter. The premise of the probelm is simple: Sort a list using the\n",
      "minimum amount of swaps")
custom_input = int(input("Would you like to enter custom input? (1) Yes (2) No"))
if custom_input == 2:
    size = int(input("Enter the input size you want to test"))
    a = np.arange(size)
    print(a)
    np.random.shuffle(a)
    print("OK. I have scrambled", size, "numbers for you.")
else:
    arr = input("Enter consecutive numbers from 0 to n-1 (for an input size of n) space seperated")
    arr = arr.split()
    arr = [int(i) for i in arr]
    a = np.array(arr)
    size = a.shape[0]


print("1.Uniform Cost Seach (size < 10 for your own sanity)")
print("2.Incorrect Tiles Heuristic")
choice = int(input("Select the algorithm you would like me to use"))

if choice == 1:
    ucs(a)
elif choice == 2:
    correct_tile_heuristic(a)



