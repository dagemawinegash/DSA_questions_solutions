# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

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
  s = string()
  stack_0 = []
  stack_1 = []
  count = 0

  ans = [0] * n
  for i in range(n):
    if s[i] == "0":
      if stack_1:
        group = stack_1.pop()
      else:
        count += 1
        group = count
      stack_0.append(group)
    else:
      if stack_0:
        group = stack_0.pop()
      else:
        count += 1
        group = count
      stack_1.append(group)
    ans[i] = group
  print(count)
  print(*ans)
        
  

    
      
        
      
      

  
  