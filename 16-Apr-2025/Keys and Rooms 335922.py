# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def helper(node):
            if visited[node]:
                return 
            visited[node] = 1
            for neighbour in rooms[node]:
                helper(neighbour)

        n = len(rooms)
        visited = [0] * n
        helper(0)
        return all(visited)

