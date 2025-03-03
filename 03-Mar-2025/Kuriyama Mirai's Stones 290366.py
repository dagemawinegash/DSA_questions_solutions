# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############

n = number()
nums1 = array()
nums2 = sorted(nums1)

for i in range(1, n):
  nums1[i] += nums1[i - 1]
  nums2[i] += nums2[i - 1]
nums1 = [0] + nums1
nums2 = [0] + nums2

m = number()

for _ in range(m):
  type, i, j = numbers()
  if type == 1:
    print(nums1[j] - nums1[i - 1])
  else:
    print(nums2[j] - nums2[i - 1])
  