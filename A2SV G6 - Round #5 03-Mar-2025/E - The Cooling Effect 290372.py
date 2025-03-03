# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

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
  white_space = string()
  n, k = numbers()
  indices = array()
  temps = array()
  forward_effect = [float('inf')] * n
  backward_effect = [float('inf')] * n
  
  for i, num in enumerate(indices):
    forward_effect[num - 1] = temps[i]
    backward_effect[num - 1] = temps[i]

  for i in range(1, n):
    if forward_effect[i] > forward_effect[i - 1] + 1:
      forward_effect[i] = forward_effect[i - 1] + 1
      
  for i in range(n - 2, -1, -1):
    if backward_effect[i] > backward_effect[i + 1] + 1:
      backward_effect[i] = backward_effect[i + 1] + 1
      
  ans = []
  for x, y in zip(forward_effect, backward_effect):
    ans.append(min(x, y))
    
  print(*ans)
  

    
  