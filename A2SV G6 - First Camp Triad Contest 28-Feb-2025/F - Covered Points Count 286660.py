# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############

q = number()

d = Counter()
for _ in range(q):
  i, j = numbers()
  d[i] += 1
  d[j + 1] -= 1

nums = sorted(d.items())
ans = [0] * (q + 1)
curr_sum = 0
for i in range(1, len(nums)):
  curr_sum += nums[i - 1][1]
  ans[curr_sum] += nums[i][0] - nums[i - 1][0]

print(*ans[1:])
  
  
    