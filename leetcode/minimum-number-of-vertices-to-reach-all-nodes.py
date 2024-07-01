class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        has_incoming_edges = set()
        ans = []

        for i in range(len(edges)):
            has_incoming_edges.add(edges[i][1])

        for node in range(n):
            if node not in has_incoming_edges:
                ans.append(node)
        return ans