# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

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

t = number()

for _ in range(t):
  n, k = numbers()
  s = string()
  nums = array()
  l = 0
  r = max(nums)

  def checker(curr_ans):
    i = 0
    res = 0
    while i < n:
      if s[i] != "R":
        if nums[i] > curr_ans:
          i += 1
          res += 1
          while i < n:
            if s[i] != "B":
              if nums[i] > curr_ans:
                break
            i += 1
      i += 1
    return res <= k
              
  ans = 0
  while l <= r:
    mid = l + (r - l) // 2
    if checker(mid):
      ans = mid
      r = mid - 1
    else:
      l = mid + 1

  print(ans)