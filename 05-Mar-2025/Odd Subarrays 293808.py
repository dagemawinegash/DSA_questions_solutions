# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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
t = number()

for _ in range(t):
  n = number()
  nums = array()
  ans = 0
  i = 0
  while i < n - 1:
    if nums[i] > nums[i + 1]:
      i += 2
      ans += 1
    else:
      i += 1
  print(ans)
    
  
  