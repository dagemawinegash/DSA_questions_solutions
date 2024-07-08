import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = set((0, 0))
        n, m = len(nums1), len(nums2)
        ans = []

        while heap and k > 0:
            sum, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            k -= 1

            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < m and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
        
        return ans



            
