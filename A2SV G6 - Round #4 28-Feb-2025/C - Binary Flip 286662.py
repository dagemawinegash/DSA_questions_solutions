# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############

def helper(n, a, b):
  flipped = False
  count = [a.count("0"), a.count("1")]
  for i in range(n - 1, -1, - 1):
    if not flipped:
      if a[i] == b[i]:
        if a[i] == "0":
          count[0] -= 1
        else:
          count[1] -= 1
      else:
        if count[0] == count[1]:
          if a[i] == "0":
            count[0] -= 1
          else:
            count[1] -= 1
          count = count[::-1]
        else:
          return "NO"
        flipped = not flipped
    else:
      if a[i] != b[i]:
        if a[i] == "0":
          count[1] -= 1
        else:
          count[0] -= 1
      else:
        if count[0] == count[1]:
          if a[i] == "0":
            count[1] -= 1
          else:
            count[0] -= 1
          count = count[::-1]
        else:
          return "NO"
        flipped = not flipped
        
  
  return "YES"
        
    

t = number()
for _ in range(t):
  print(helper(number(), string(), string()))