# Problem: H - Dominoes - https://codeforces.com/gym/589822/problem/H

############ ---- Functions for inputs ---- ############
import math
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter


def number():
    return int(input())


def numbers():
    return map(int, input().split())


def array():
    return list(map(int, input().split()))


def string():
    return input()


############ ---- Functions for inputs ---- ############

rows, cols = numbers()
grid = []
for _ in range(rows):
    grid.append(list(string()))

horizontal = [[0] * (cols + 1) for _ in range(rows + 1)]
vertical = [[0] * (cols + 1) for _ in range(rows + 1)]

for i in range(rows):
    for j in range(cols):
        if j > 0 and grid[i][j] == "." and grid[i][j - 1] == ".":
            horizontal[i + 1][j + 1] = 1
        if i > 0 and grid[i][j] == "." and grid[i - 1][j] == ".":
            vertical[i + 1][j + 1] = 1

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        horizontal[i][j] += horizontal[i][j - 1]
        vertical[i][j] += vertical[i][j - 1]

for j in range(1, cols + 1):
    for i in range(1, rows + 1):
        horizontal[i][j] += horizontal[i - 1][j]
        vertical[i][j] += vertical[i - 1][j]

# print(horizontal)
# print(vertical)
q = number()
for _ in range(q):
    a, b, c, d = numbers()
    hor = horizontal[c][d] - horizontal[c][b] - horizontal[a - 1][d] + horizontal[a - 1][b]
    ver = vertical[c][d] - vertical[c][b - 1] - vertical[a][d] + vertical[a][b - 1]

    print(hor + ver)
