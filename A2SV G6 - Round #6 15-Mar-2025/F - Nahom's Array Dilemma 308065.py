# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############

def helper(n, nums):
  stack = []
  prefix = [nums[0]]
  for i in range(1, n):
    prefix.append(prefix[i - 1] + nums[i])
  prefix = [0] + prefix

  for i in range(n):
    while stack and nums[i] >= nums[stack[-1]]:
      idx = stack.pop()
      if prefix[i + 1] - prefix[idx] > nums[i]:
        return False
    stack.append(i)
  return True


t = number()
for _ in range(t):
  n = number()
  nums = array()
  left = helper(n, nums)
  right = helper(n, nums[::-1])
  if left and right:
    print("YES")
  else:
    print("NO")
    