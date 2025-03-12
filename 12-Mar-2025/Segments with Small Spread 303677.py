# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############

n, k = numbers()
nums = array()
max_queue = deque()
min_queue = deque()
ans = 0
start = 0
for end, num in enumerate(nums):
  while max_queue and nums[max_queue[-1]] < num:
    max_queue.pop()
  max_queue.append(end)
  while min_queue and nums[min_queue[-1]] > num:
    min_queue.pop()
  min_queue.append(end)
  while max_queue and min_queue and nums[max_queue[0]] - nums[min_queue[0]] > k:
    if min_queue and start == min_queue[0]:
      min_queue.popleft()
    if max_queue and start == max_queue[0]:
      max_queue.popleft()
    start += 1
  ans += end - start + 1

print(ans)
      
