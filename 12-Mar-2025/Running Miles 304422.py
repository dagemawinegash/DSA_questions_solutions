# Problem: Running Miles - https://codeforces.com/problemset/problem/1826/D

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
  n = number()
  nums = array()
  
  if n < 3:
    print(0)
    continue

  prefix = [float('-inf')] * n
  prefix[0] = nums[0] 
  
  for i in range(1, n):
    prefix[i] = max(prefix[i - 1], nums[i] + i)
  
  suffix = [float('-inf')] * n
  suffix[-1] = nums[-1] - (n - 1) 

  for i in range(n - 2, -1, -1):
    suffix[i] = max(suffix[i + 1], nums[i] - i)
  
  ans = float('-inf')
  
  # print(prefix)
  # print(suffix)
  for i in range(1, n - 1): 
    ans = max(ans, nums[i] + prefix[i - 1] + suffix[i + 1])
  
  print(ans)

      
    
  
  
  

      
    