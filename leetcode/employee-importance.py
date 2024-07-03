class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        dictionary = {}

        for emp in employees:
            dictionary[emp.id] = emp
        
        def dfs(emp_id):
            emp = dictionary[emp_id]
            tot_imp = emp.importance

            for sub in emp.subordinates:
                tot_imp += dfs(sub)
            
            return tot_imp
            
        return dfs(id)




        