# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

############ ---- Functions for inputs ---- ############
from math import *
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
  t = number()
  for _ in range(t):
    s = string()
    q = number()
    queries = array()
    n = len(s)
    
    def helper(q, curr):
      if 1 <= q <= n:
        return s[q - 1]
      
      while q > curr:
        curr *= 2
      
      if q > curr // 2:
        char = helper(q - (curr // 2), curr // 2)
        return char.swapcase()
      else:
        return helper(q, curr // 2)
    
    ans = []
    for q in queries:
      
      ans.append(helper(q, n))
    print(*ans)

main()
      