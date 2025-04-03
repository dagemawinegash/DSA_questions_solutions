# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############

t = number()

for _ in range(t):
  n, m = numbers()
  nums = array()
  offsets = sorted(array())
  
  def helper(i):
    res = -1
    l, r = 0, m - 1
    while l <= r:
      mid = l + (r - l) // 2
      val = offsets[mid] - nums[i]
      if val >= ans[-1]:
        res = mid
        r = mid - 1 
      else:
        l = mid + 1
    return res
  
  ans = [min(nums[0], offsets[0] - nums[0])]
  for i in range(1, n):
      idx = helper(i)
      if 0 <= idx < m:
        x = min(offsets[idx] - nums[i], nums[i])
        y = max(offsets[idx] - nums[i], nums[i])
        ans.append(x if x >= ans[-1] else y)
      else:
        ans.append(nums[i]) 
    
  if ans == sorted(ans):
    print("YES")
  else:
    print("NO")