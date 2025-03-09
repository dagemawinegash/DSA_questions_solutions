# Problem: F - The Last Problem - https://codeforces.com/gym/591928/problem/F

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
a = array()
b = array()
total = 0

for i in range(n):
  total += a[i] * b[i]
  
ans = total

def inbound(i, j):
  return (0 <= i < n) and (0 <= j < n)

# creating odd length sub-arrays
for idx in range(n):
  i = idx - 1
  j = idx + 1
  curr = total
  while inbound(i, j):
    curr -= ((a[i] * b[i]) + (a[j] * b[j]))
    curr += ((a[i] * b[j]) + (a[j] * b[i]))
    ans = max(ans, curr)
    i -= 1
    j += 1

# creating even length sub-arrays
for idx in range(n):
  i = idx
  j = idx + 1
  curr = total
  while inbound(i, j):
    curr -= ((a[i] * b[i]) + (a[j] * b[j]))
    curr += ((a[i] * b[j]) + (a[j] * b[i]))
    ans = max(ans, curr)
    i -= 1
    j += 1

print(ans)

  