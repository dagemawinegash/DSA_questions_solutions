# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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
  nums1 = array()
  m = number()
  nums2 = array()

  for i in range(1, n):
    nums1[i] += nums1[i - 1]

  for i in range(1, m):
    nums2[i] += nums2[i - 1]

  print(max(0, max(nums1)) + max(0, max(nums2)))