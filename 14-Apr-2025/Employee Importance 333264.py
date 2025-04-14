# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for data in employees:
            d[data.id] = data

        ans = 0
        def helper(id):
            nonlocal ans
            emp = d[id]
            ans += emp.importance
            for neighbour in emp.subordinates:
                helper(neighbour)
        helper(id)
        return ans

        