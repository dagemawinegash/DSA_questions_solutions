# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
import random
RANDOM_SEED = random.randint(10**5, 10**6)

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############


import sys
import threading
input_fn = lambda: sys.stdin.readline().strip()

def main():
  def helper(start, end, good):
    if end == start:
      if s[end] == good:
        return 0
      else:
        return 1

    idx = (end + start) // 2
    
    op_first = 0
    for i in range(start, idx + 1):
      if s[i] != good:
        op_first += 1
        
    op_second = 0
    for i in range(idx + 1, end + 1):
      if s[i] != good:
        op_second += 1
        
    option1 = op_first + helper(idx + 1, end, chr(ord(good) + 1))
    option2 = op_second + helper(start, idx, chr(ord(good) + 1))

    return min(option1, option2)
    

  t = number()
  for _ in range(t):
    n = number()
    s = string()
    print(helper(0, n - 1, "a"))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
