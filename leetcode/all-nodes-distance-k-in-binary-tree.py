from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        graph = defaultdict(list)

        def traverse(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                traverse(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                traverse(node.right)

        traverse(root)

        queue = deque()
        queue.append([target.val, 0])
        visited = set()
        visited.add(target.val)
        ans = []
        while queue:
            node_val, steps = queue.popleft()
            if steps == k:
                ans.append(node_val)

            for neighbour in graph[node_val]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append([neighbour, steps + 1])

        return ans

        