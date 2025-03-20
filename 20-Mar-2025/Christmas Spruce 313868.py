# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

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

def helper(d):
  parents = list(d.keys())
  # print(parents)
  # print(d)
  for parent in d:
    count = 0
    children = d[parent]
    for child in children:
      if child in parents:
        count += 1
    if len(children) - count < 3:
      return "No"
  return "Yes"

n = number()
curr = 2
d = defaultdict(list)

for _ in range(n - 1):
  num = number()
  d[num].append(curr)
  curr += 1
# print(d)
print(helper(d))