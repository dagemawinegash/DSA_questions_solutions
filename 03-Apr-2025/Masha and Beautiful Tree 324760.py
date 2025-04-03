# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
  n = number()
  nums = array()
  ans = 0
  def merge(left, right):
    global ans
    if left[0] < right[0]:
      return left + right
    else:
      ans += 1
      return right + left
    
  def mergeSort(l, r):
    if l == r:
      return [nums[l]]
    
    mid = l + (r - l) // 2
    left_side = mergeSort(l, mid)
    right_side = mergeSort(mid + 1, r)
    return merge(left_side, right_side)

  res = mergeSort(0, n - 1)
  if res == sorted(res):
    print(ans)
  else:     
    print(-1)
    