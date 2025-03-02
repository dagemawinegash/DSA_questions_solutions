# Problem: E - Weird and Ugly Monsters - https://codeforces.com/gym/590053/problem/E

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter

def number(): return(int(input()))
def numbers(): return(map(int,input().split()))
def array(): return(list(map(int,input().split())))
def string(): return input()
############ ---- Functions for inputs ---- ############

class Node:
  def __init__(self, idx, ugliness):
    self.idx = idx
    self.ugliness = ugliness
    self.nxt = None
    self.prev = None

def merge(curr, cnt):
  while True:
    merged = False
    if curr.prev != curr and curr.ugliness == curr.prev.ugliness:
      left = curr.prev
      if curr.idx > left.idx:
        left.nxt = curr.nxt
        curr.nxt.prev = left
        left.ugliness *= 2
        cnt[0] -= 1
        curr = left
      else:
        curr.prev = left.prev
        left.prev.nxt = curr
        curr.ugliness *= 2
        cnt[0] -= 1
      merged = True
    elif curr.nxt != curr and curr.ugliness == curr.nxt.ugliness:
      right = curr.nxt
      if curr.idx > right.idx:
        curr.prev.nxt = right
        right.prev = curr.prev
        right.ugliness *= 2
        cnt[0] -= 1
        curr = right
      else:
        right.nxt.prev = curr
        curr.nxt = right.nxt
        curr.ugliness *= 2
        cnt[0] -= 1
      merged = True
    if not merged:
      break

def helper():
  n, p = numbers()
  cnt = [1]
  head = Node(1, p)
  head.nxt = head
  head.prev = head
  track = {1: head}
  idx_list = array()
  ugliness_list = array()
  nxt_idx = 2
  ans = []
  for i in range(n):
    pos, ugliness = idx_list[i], ugliness_list[i]
    ref = track[pos]
    new_node = Node(nxt_idx, ugliness)
    nxt_idx += 1
    new_node.nxt = ref.nxt
    new_node.prev = ref
    ref.nxt.prev = new_node
    ref.nxt = new_node
    track[new_node.idx] = new_node
    cnt[0] += 1
    merge(new_node, cnt)
    ans.append(cnt[0])
  print(*ans)

t = number()
for _ in range(t):
  helper()