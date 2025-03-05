# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
import random
RANDOM_SEED = random.randint(10**5, 10**6)

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############

n, k = numbers()
nums = array()
arr = []
for i in range(n - 1):
  arr.append(nums[i + 1] - nums[i])
arr.sort(reverse=True)
print(sum(arr[k - 1:]))



  