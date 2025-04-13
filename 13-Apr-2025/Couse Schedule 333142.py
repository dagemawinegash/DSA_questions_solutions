# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:  
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # print(graph)

        def detect_cycle(node):
            visited[node] = 1
            path_visited[node] = 1
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if detect_cycle(neighbour):
                        return True
                else:
                    if path_visited[neighbour]:
                        return True
            path_visited[node] = 0
            return False

        visited = [0] * numCourses
        path_visited = [0] * numCourses
        for node in range(numCourses):
            if not visited[node]:
                if detect_cycle(node):
                    return False
        return  True


